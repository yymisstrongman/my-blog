import uvicorn
import json
import os
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
import uuid

# ================= 配置 =================
SECRET_KEY = "随便填一串长随机字符，比如d9s28gh329ghsdgj239"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
app = FastAPI(title="个人博客后端")

# 跨域配置，部署时改成你的前端域名
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yymisstrongman.github.io/my-blog/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据持久化文件
USERS_FILE = "users.json"
POSTS_FILE = "posts.json"
COUNTER_FILE = "counter.json"

# ================= 持久化读写函数 =================
def load_data():
    global users_db, posts_db, post_id_counter
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            users_db = json.load(f)
    else:
        users_db = {}
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            posts_db = json.load(f)
    else:
        posts_db = []
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r", encoding="utf-8") as f:
            post_id_counter = json.load(f)["counter"]
    else:
        post_id_counter = 1

def save_all():
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users_db, f, ensure_ascii=False, indent=2)
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts_db, f, ensure_ascii=False, indent=2)
    with open(COUNTER_FILE, "w", encoding="utf-8") as f:
        json.dump({"counter": post_id_counter}, f)

# 初始化数据
users_db = {}
posts_db = []
post_id_counter = 1
load_data()

# ================= 密码、JWT工具 =================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ================= 模型 =================
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: str
    username: str
    email: str

class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    author: UserOut

# ================= 关键：关闭公开注册接口 =================
@app.post("/register", response_model=UserOut)
async def register():
    # 直接返回禁止注册，游客无法注册账号
    raise HTTPException(status_code=403, detail="网站关闭公开注册，仅管理员可登录发布文章")

# 手动添加管理员函数（你本地运行一次创建账号，之后注释掉）
def create_admin(username: str, email: str, password: str):
    if username in users_db:
        print("管理员已存在")
        return
    user_id = str(uuid.uuid4())
    new_user = {
        "id": user_id,
        "username": username,
        "email": email,
        "hashed_password": get_password_hash(password)
    }
    users_db[username] = new_user
    save_all()
    print("管理员创建成功")

# ================= 登录接口（仅管理员可用） =================
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# 获取当前登录用户
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="未登录")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = users_db.get(username)
    if user is None:
        raise credentials_exception
    return user

# 所有人都能查看文章列表
@app.get("/posts", response_model=List[PostOut])
async def get_posts():
    sorted_posts = sorted(posts_db, key=lambda x: x["created_at"], reverse=True)
    result = []
    for post in sorted_posts:
        author = users_db.get(post["author_username"])
        result.append(PostOut(
            id=post["id"],
            title=post["title"],
            content=post["content"],
            created_at=post["created_at"],
            author=UserOut(id=author["id"], username=author["username"], email=author["email"])
        ))
    return result

# 所有人都能看单篇文章
@app.get("/posts/{post_id}", response_model=PostOut)
async def get_post(post_id: str):
    for post in posts_db:
        if post["id"] == post_id:
            author = users_db.get(post["author_username"])
            return PostOut(
                id=post["id"],
                title=post["title"],
                content=post["content"],
                created_at=post["created_at"],
                author=UserOut(id=author["id"], username=author["username"], email=author["email"])
            )
    raise HTTPException(status_code=404, detail="文章未找到")

# 只有登录管理员才能发布文章
@app.post("/posts", response_model=PostOut)
async def create_post(post: PostCreate, current_user: dict = Depends(get_current_user)):
    global post_id_counter
    new_post = {
        "id": str(post_id_counter),
        "title": post.title,
        "content": post.content,
        "author_username": current_user["username"],
        "created_at": datetime.now()
    }
    post_id_counter += 1
    posts_db.append(new_post)
    save_all()
    return PostOut(
        id=new_post["id"],
        title=new_post["title"],
        content=new_post["content"],
        created_at=new_post["created_at"],
        author=UserOut(id=current_user["id"], username=current_user["username"], email=current_user["email"])
    )

# 静态页面挂载（前后端放同一台国内服务器时使用）
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    # ========== 第一次运行取消注释，创建你的管理员账号 ==========
    # create_admin("你的账号名", "你的邮箱", "你的密码")
    # ======================================================
    uvicorn.run(app, host="0.0.0.0", port=8000)
