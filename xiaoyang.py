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

# ================= 配置区 =================
SECRET_KEY = "ksdfh2398ghasd723hgasd923ghsa9123hd"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
app = FastAPI(title="个人博客后端")

# 跨域固定填你的GitHub Pages地址，无需修改
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://yymisstrongman.github.io/my-blog/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 持久化存储文件
USERS_FILE = "users.json"
POSTS_FILE = "posts.json"
COUNTER_FILE = "counter.json"

# ================= 数据读写函数 =================
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

# 全局初始化数据
users_db = {}
posts_db = []
post_id_counter = 1
load_data()

# ================= 密码与Token工具 =================
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

# ================= 数据模型 =================
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

# ================= 注册接口：关闭公开注册 =================
@app.post("/register", response_model=UserOut)
async def register():
    raise HTTPException(status_code=403, detail="网站关闭公开注册，仅管理员可登录发布文章")

# 创建管理员函数（仅首次运行启用）
def create_admin(username: str, email: str, password: str):
    if username in users_db:
        print("管理员账号已存在，无需重复创建")
        return
    user_id = str(uuid.uuid4())
    new_user = {
        "id": user_id,
        "username": username,
        "email": "1828721908@qq.com",
        "hashed_password": get_password_hash(password)
    }
    users_db[username] = new_user
    save_all()
    print("✅ 管理员账号创建成功！")

# ================= 登录接口 =================
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="用户名或密码错误")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# 获取当前登录管理员
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="未登录，请先登录管理员账号")
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

# 所有人均可查看文章列表
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

# 所有人均可查看单篇文章详情
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
    raise HTTPException(status_code=404, detail="文章不存在")

# 仅登录管理员可发布文章
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

# 本地服务器挂载静态页面（Replit无需此功能，保留不影响运行）
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    # ========== 第一次运行请删除本行#，运行一次生成账号 ==========
    create_admin("xiaoyangstrongman", "1828721908@qq.com", "1838543866687")
    # =================================================================
    uvicorn.run(app, host="0.0.0.0", port=8000)