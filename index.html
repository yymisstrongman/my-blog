<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>小杨的博客</title>
    <!-- 网址栏图标 = 你的头像 -->
    <link rel="icon" href="https://raw.githubusercontent.com/yymisstrongman/my-blog/main/avatar.jpg" type="image/jpeg">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <style>
        :root {
            --bg: #f4f6f9;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --accent: #2563eb;
            --border: #e2e8f0;
            --card-bg: rgba(255, 255, 255, 0.7);
        }
        * {margin: 0;padding: 0;box-sizing: border-box;}
        body {background: var(--bg);min-height: 100vh;color: var(--text-primary);}
        nav {position: fixed;top: 0;left: 0;right: 0;z-index: 100;background: rgba(255,255,255,0.85);backdrop-filter: blur(12px);border-bottom: 1px solid var(--border);}
        .nav-container {max-width: 900px;margin: 0 auto;padding: 1.25rem 2rem;display: flex;justify-content: space-between;align-items: center;}
        .nav-brand {font-size: 1.25rem;font-weight: 700;color: var(--text-primary);cursor: pointer;letter-spacing: -0.5px;}
        .nav-links {display: flex;align-items: center;gap: 2rem;}
        .nav-link {color: var(--text-secondary);text-decoration: none;font-size: 0.95rem;font-weight: 500;transition: color 0.2s;cursor: pointer;}
        .nav-link:hover {color: var(--accent);}
        .nav-icon {color: var(--text-secondary);cursor: pointer;transition: color 0.2s;display: flex;align-items: center;}
        .nav-icon:hover {color: var(--accent);}
        main {max-width: 900px;margin: 0 auto;padding: 6rem 2rem 4rem;}
        .page {display: none;animation: fadeIn 0.3s ease;}
        .page.active {display: block;}
        @keyframes fadeIn {from {opacity: 0;transform: translateY(10px);}to {opacity: 1;transform: translateY(0);}}
        .hero {text-align: center;padding: 3rem 0 2rem;}
        .avatar {width: 120px;height: 120px;border-radius: 50%;border: 2px solid var(--border);object-fit: cover;box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);}
        .name {font-size: 2.5rem;font-weight: 700;margin-top: 1.5rem;letter-spacing: -1px;color: var(--text-primary);}
        .meta {display: flex;justify-content: center;align-items: center;gap: 2rem;margin-top: 1rem;color: var(--text-secondary);font-size: 0.95rem;}
        .meta-item {display: flex;align-items: center;gap: 0.5rem;}
        .meta a {color: var(--text-secondary);text-decoration: none;transition: color 0.2s;}
        .meta a:hover {color: var(--accent);}
        .section {display: flex;gap: 3rem;margin-top: 4rem;align-items: flex-start;}
        .section-title {width: 140px;text-align: right;font-size: 1.5rem;font-weight: 700;color: var(--text-primary);padding-top: 0.25rem;flex-shrink: 0;}
        .section-content {flex: 1;min-width: 0;}
        .tags {color: var(--text-secondary);font-size: 1.05rem;margin-bottom: 1.25rem;line-height: 1.8;}
        .tags del {text-decoration: line-through;opacity: 0.5;}
        .bio {color: var(--text-secondary);line-height: 1.9;font-size: 1.05rem;}
        .bio p {margin-bottom: 0.75rem;}
        .codetime {display: inline-flex;align-items: center;gap: 0.5rem;background: #ffffff;padding: 0.4rem 0.8rem;border-radius: 6px;font-size: 0.85rem;color: var(--text-secondary);margin-top: 1.5rem;border: 1px solid var(--border);box-shadow: 0 1px 2px rgba(0,0,0,0.05);}
        .more-btn {display: inline-block;margin-top: 1.5rem;padding: 0.6rem 1.25rem;border: 1px solid var(--border);border-radius: 6px;color: var(--text-secondary);text-decoration: none;font-size: 0.9rem;transition: all 0.2s;cursor: pointer;background: #ffffff;}
        .more-btn:hover {border-color: var(--accent);color: var(--accent);background: #f8fafc;}
        .posts-list {display: flex;flex-direction: column;gap: 0.75rem;}
        .post-item {display: flex;align-items: center;padding: 1rem 1.25rem;border-radius: 8px;cursor: pointer;transition: all 0.2s ease;border: 1px solid transparent;background: #ffffff;box-shadow: 0 1px 2px rgba(0,0,0,0.05);}
        .post-item:hover {border-color: var(--accent);transform: translateX(4px);box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);}
        .post-date {width: 110px;flex-shrink: 0;color: var(--text-secondary);font-size: 0.875rem;font-variant-numeric: tabular-nums;}
        .post-title {flex: 1;color: var(--text-primary);font-size: 1.05rem;font-weight: 500;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;}
        .post-arrow {color: var(--text-secondary);font-size: 1.25rem;transition: color 0.2s;margin-left: 0.5rem;}
        .post-item:hover .post-arrow {color: var(--accent);}
        .empty-state {color: var(--text-secondary);padding: 2rem 0;font-size: 0.95rem;background: #ffffff;border-radius: 8px;text-align: center;border: 1px dashed var(--border);}
        .detail-header {margin-bottom: 2rem;}
        .back-link {color: var(--accent);cursor: pointer;display: inline-flex;align-items: center;gap: 0.5rem;font-size: 0.95rem;margin-bottom: 1.5rem;transition: opacity 0.2s;}
        .back-link:hover {opacity: 0.8;}
        .detail-title {font-size: 2rem;font-weight: 700;margin-bottom: 0.75rem;line-height: 1.3;}
        .detail-meta {color: var(--text-secondary);font-size: 0.9rem;display: flex;gap: 1.5rem;flex-wrap: wrap;}
        .detail-content {color: var(--text-secondary);line-height: 1.9;font-size: 1.05rem;margin-top: 2rem;padding-top: 2rem;border-top: 1px solid var(--border);}
        .form-page {max-width: 480px;margin: 3rem auto 0;}
        .form-card {background: #ffffff;padding: 2.5rem;border-radius: 12px;border: 1px solid var(--border);box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);}
        .form-card h2 {margin-bottom: 1.75rem;font-size: 1.5rem;text-align: center;color: var(--text-primary);}
        .form-group {margin-bottom: 1.25rem;}
        label {display: block;margin-bottom: 0.5rem;color: var(--text-secondary);font-size: 0.9rem;}
        input, textarea {width: 100%;padding: 0.85rem 1rem;background: #f8fafc;border: 1px solid var(--border);border-radius: 6px;color: var(--text-primary);font-size: 1rem;font-family: inherit;transition: border-color 0.2s;}
        input:focus, textarea:focus {outline: none;border-color: var(--accent);background: #ffffff;}
        textarea {min-height: 240px;resize: vertical;}
        .btn-primary {width: 100%;padding: 0.85rem;background: var(--accent);border: 1px solid var(--accent);border-radius: 6px;color: #ffffff;font-size: 1rem;font-weight: 600;cursor: pointer;transition: all 0.2s;margin-top: 0.5rem;}
        .btn-primary:hover {background: #1d4ed8;border-color: #1d4ed8;}
        .form-toggle {text-align: center;margin-top: 1.25rem;color: var(--accent);cursor: pointer;font-size: 0.9rem;}
        .form-toggle:hover {text-decoration: underline;}
        .error-msg {color: #ef4444;font-size: 0.875rem;margin-top: 0.5rem;}
        .project-grid {display: grid;grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));gap: 1.5rem;margin-top: 1rem;}
        .project-card {background: #ffffff;padding: 1.5rem;border-radius: 8px;border: 1px solid var(--border);transition: all 0.2s;}
        .project-card:hover {border-color: var(--accent);transform: translateY(-4px);box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);}
        .project-card h3 {font-size: 1.1rem;margin-bottom: 0.5rem;}
        .project-card p {color: var(--text-secondary);font-size: 0.9rem;line-height: 1.6;}
        .link-list {display: flex;flex-direction: column;gap: 0.75rem;}
        .link-item {display: flex;align-items: center;padding: 0.8rem 1rem;background: #ffffff;border-radius: 6px;border: 1px solid var(--border);transition: all 0.2s;text-decoration: none;color: var(--text-primary);}
        .link-item:hover {border-color: var(--accent);background: #f8fafc;}
        .link-item .link-icon {margin-right: 0.75rem;font-size: 1.2rem;}
        .link-item .link-name {flex: 1;font-weight: 500;}
        .link-item .link-desc {color: var(--text-secondary);font-size: 0.85rem;}
        .search-box {max-width: 600px;margin: 2rem auto 0;}
        .search-box input {padding: 0.85rem 1.2rem;font-size: 1rem;border-radius: 30px;border: 1px solid var(--border);background: #ffffff;width: 100%;outline: none;transition: border-color 0.2s;}
        .search-box input:focus {border-color: var(--accent);}
        .search-results {margin-top: 2rem;}
        .search-result-item {padding: 0.8rem 1rem;background: #ffffff;border-bottom: 1px solid var(--border);cursor: pointer;transition: background 0.2s;}
        .search-result-item:hover {background: #f1f5f9;}
        .search-result-item .title {font-weight: 500;color: var(--text-primary);}
        .search-result-item .date {color: var(--text-secondary);font-size: 0.8rem;margin-left: 1rem;}
        .token-modal {position: fixed;top: 0;left: 0;right: 0;bottom: 0;background: rgba(0,0,0,0.5);display: flex;align-items: center;justify-content: center;z-index: 999;display: none;}
        .token-card {background: white;padding: 2rem;border-radius: 8px;width: 90%;max-width: 400px;}
        .token-card h3 {margin-bottom: 1rem;text-align: center;}
        @media (max-width: 768px) {
            .nav-links {gap: 1.25rem;}
            main {padding: 5rem 1.5rem 3rem;}
            .section {flex-direction: column;gap: 1.5rem;margin-top: 3rem;}
            .section-title {width: 100%;text-align: left;font-size: 1.25rem;}
            .name {font-size: 2rem;}
            .meta {flex-direction: column;gap: 0.5rem;}
            .post-item {flex-direction: column;align-items: flex-start;gap: 0.25rem;}
            .post-date {width: auto;font-size: 0.8rem;}
            .project-grid {grid-template-columns: 1fr 1fr;}
        }
        @media (max-width: 480px) {
            .project-grid {grid-template-columns: 1fr;}
        }
    </style>
</head>
<body>
<div id="tokenModal" class="token-modal">
    <div class="token-card">
        <h3>GitHub Access Token</h3>
        <div class="form-group">
            <label>请输入GitHub Personal Access Token</label>
            <input type="password" id="githubToken" placeholder="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx">
            <small style="color: var(--text-secondary); font-size: 0.8rem; margin-top: 0.5rem; display: block;">
                需开启 repo 权限，创建地址：<a href="https://github.com/settings/tokens" target="_blank">https://github.com/settings/tokens</a>
            </small>
        </div>
        <div id="tokenError" class="error-msg"></div>
        <button class="btn-primary" onclick="saveToken()">确认</button>
    </div>
</div>
<nav>
    <div class="nav-container">
        <div class="nav-brand" onclick="showPage('home')">小杨's Blog</div>
        <div class="nav-links">
            <a class="nav-link" onclick="showPage('home')">Blog</a>
            <a class="nav-link" onclick="showPage('projects')">Projects</a>
            <a class="nav-link" onclick="showPage('links')">Links</a>
            <a class="nav-link" onclick="showPage('about')">About</a>
            <span class="nav-icon" title="搜索" onclick="showPage('search')">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
            </span>
            <span class="nav-icon" title="发布文章" onclick="checkTokenAndShowCreate()">
                <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8m-4-4v4"/></svg>
            </span>
            <span id="navAuth">
                <a class="nav-link" onclick="logout()">退出</a>
            </span>
        </div>
    </div>
</nav>
<main>
    <div id="page-home" class="page active">
        <div class="hero">
            <img src="https://raw.githubusercontent.com/yymisstrongman/my-blog/main/avatar.jpg" alt="头像" class="avatar">
            <h1 class="name">小杨</h1>
            <div class="meta">
                <div class="meta-item">
                    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                    <span>China / 渭南</span>
                </div>
                <div class="meta-item">
                    <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    <a href="https://github.com/yymisstrongman" target="_blank">GitHub</a>
                </div>
            </div>
        </div>
        <div class="section">
            <div class="section-title">Posts</div>
            <div class="section-content">
                <div id="postsList" class="posts-list">
                    <div class="empty-state">加载中...</div>
                </div>
            </div>
        </div>
    </div>
    <div id="page-detail" class="page">
        <div class="detail-header">
            <div class="back-link" onclick="showPage('home')">
                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 12H5m7 7-7-7 7-7"/></svg>
                返回文章列表
            </div>
            <h1 id="detailTitle" class="detail-title"></h1>
            <div id="detailMeta" class="detail-meta"></div>
        </div>
        <div id="detailContent" class="detail-content"></div>
    </div>
    <div id="page-about" class="page">
        <div class="hero" style="padding-bottom: 0;">
            <h2 style="font-size: 2rem; font-weight: 700;">👋 关于我</h2>
        </div>
        <div class="section" style="margin-top: 1rem;">
            <div class="section-title">About</div>
            <div class="section-content">
                <div class="tags">信息安全 / 渭南师范学院 / <del>CTFer</del></div>
                <div class="bio">
                    <p>大家好我是小杨，一名渭南师范学院的信息安全专业的学生。</p>
                    <p>正在努力学习网络安全、二进制安全以及Web安全。</p>
                    <p>这个是我的博客，以后会持续更新我的学习进度，欢迎大家莅临指导。</p>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                    <div class="codetime">
                        <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                        持续更新学习中...
                    </div>
                    <button class="more-btn" onclick="alert('欢迎交流！')">联系我</button>
                </div>
            </div>
        </div>
    </div>
    <div id="page-projects" class="page">
        <div class="hero" style="padding-bottom: 1rem;">
            <h2 style="font-size: 2rem; font-weight: 700;">🚀 我的项目</h2>
            <p style="color: var(--text-secondary); margin-top: 0.5rem;">一些个人练习和开源贡献</p>
        </div>
        <div class="project-grid">
            <div class="project-card">
                <h3>🔐 二进制漏洞挖掘</h3>
                <p>基于 AFL 的 fuzzing 实验，发现多个 CVE 漏洞。</p>
            </div>
            <div class="project-card">
                <h3>🌐 个人博客系统</h3>
                <p>使用 FastAPI + SQLite + Vanilla JS 构建，支持 Markdown 发布。</p>
            </div>
            <div class="project-card">
                <h3>🛡️ Web 安全靶场</h3>
                <p>包含 SQL 注入、XSS、CSRF 等常见漏洞的 Docker 环境。</p>
            </div>
            <div class="project-card">
                <h3>📊 网络流量分析</h3>
                <p>基于 Scapy 的 pcap 包解析与异常检测工具。</p>
            </div>
        </div>
    </div>
    <div id="page-links" class="page">
        <div class="hero" style="padding-bottom: 1rem;">
            <h2 style="font-size: 2rem; font-weight: 700;">🔗 友情链接</h2>
            <p style="color: var(--text-secondary); margin-top: 0.5rem;">一些值得关注的站点</p>
        </div>
        <div class="link-list">
            <a href="https://github.com" target="_blank" class="link-item">
                <span class="link-icon">🐙</span>
                <span class="link-name">GitHub</span>
                <span class="link-desc">全球最大的代码托管平台</span>
            </a>
            <a href="https://www.kali.org" target="_blank" class="link-item">
                <span class="link-icon">💀</span>
                <span class="link-name">Kali Linux</span>
                <span class="link-desc">渗透测试专用操作系统</span>
            </a>
            <a href="https://portswigger.net/web-security" target="_blank" class="link-item">
                <span class="link-icon">🛡️</span>
                <span class="link-name">PortSwigger Web Security</span>
                <span class="link-desc">Web 安全权威学习资源</span>
            </a>
            <a href="https://www.ctfhub.com" target="_blank" class="link-item">
                <span class="link-icon">🏁</span>
                <span class="link-name">CTFHub</span>
                <span class="link-desc">CTF 技能树和练习平台</span>
            </a>
        </div>
    </div>
    <div id="page-search" class="page">
        <div class="hero" style="padding-bottom: 1rem;">
            <h2 style="font-size: 2rem; font-weight: 700;">🔍 搜索文章</h2>
            <p style="color: var(--text-secondary); margin-top: 0.5rem;">输入关键词，快速找到你感兴趣的内容</p>
        </div>
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="输入标题关键词..." oninput="filterPosts()">
            <div id="searchResults" class="search-results">
                <div class="empty-state">输入关键词开始搜索</div>
            </div>
        </div>
    </div>
    <div id="page-create" class="page">
        <div class="form-page">
            <div class="form-card">
                <h2>发布新文章</h2>
                <div class="form-group">
                    <label>标题</label>
                    <input type="text" id="createTitle" placeholder="文章标题">
                </div>
                <div class="form-group">
                    <label>内容（支持Markdown）</label>
                    <textarea id="createContent" placeholder="支持 Markdown 语法..."></textarea>
                </div>
                <div id="createError" class="error-msg"></div>
                <button class="btn-primary" onclick="handleCreate()">立即发布</button>
            </div>
        </div>
    </div>
</main>
<script>
// ============ 已为你填好配置，不用改任何东西 ============
const CONFIG = {
    githubUsername: "yymisstrongman",
    repoName: "my-blog",
    branch: "main",
    avatarUrl: "https://raw.githubusercontent.com/yymisstrongman/my-blog/main/avatar.jpg"
};
let allPostsCache = [];
function formatDate(isoString){const d=new Date(isoString);const m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];return `${m[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;}
function escapeHtml(t){if(!t)return '';const d=document.createElement('div');d.textContent=t;return d.innerHTML;}
function getToken(){return localStorage.getItem('github_token');}
function saveToken(){const t=document.getElementById('githubToken').value.trim();const e=document.getElementById('tokenError');if(!t||!t.startsWith('ghp_')){e.textContent='请输入有效的GitHub Token（ghp_开头）';return;}localStorage.setItem('github_token',t);document.getElementById('tokenModal').style.display='none';showPage('create');}
function checkTokenAndShowCreate(){const t=getToken();if(t){showPage('create');}else{document.getElementById('tokenModal').style.display='flex';document.getElementById('githubToken').value='';document.getElementById('tokenError').textContent='';}}
function logout(){localStorage.removeItem('github_token');alert('已退出，发文章需重新填写Token');showPage('home');}
function showPage(n,p){document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.getElementById('page-'+n).classList.add('active');window.scrollTo(0,0);if(n==='home')loadPosts();else if(n==='detail'&&p)loadDetail(p);else if(n==='search')loadPostsForSearch();}
async function loadPosts(){const box=document.getElementById('postsList');box.innerHTML='<div class="empty-state">加载中...</div>';try{const res=await axios({url:`https://api.github.com/repos/${CONFIG.githubUsername}/${CONFIG.repoName}/contents/`,method:'GET',headers:{Accept:'application/vnd.github.v3+json'}});const md=res.data.filter(f=>f.name.endsWith('.md'));const list=await Promise.all(md.map(async f=>{const d=await axios({url:f.url,method:'GET',headers:{Accept:'application/vnd.github.v3+json'}});return {id:f.sha,title:f.name.replace('.md',''),created_at:d.data.created_at,download_url:f.download_url};}));list.sort((a,b)=>new Date(b.created_at)-new Date(a.created_at));allPostsCache=list;if(!list.length){box.innerHTML='<div class="empty-state">还没有文章，登录后发布第一篇吧 ✍️</div>';return;}box.innerHTML=list.map(post=>`<div class="post-item" onclick="showPage('detail','${post.id}')"><div class="post-date">${formatDate(post.created_at)}</div><div class="post-title">${escapeHtml(post.title)}</div><div class="post-arrow">&rsaquo;</div></div>`).join('');}catch(err){console.error(err);box.innerHTML='<div class="empty-state">加载失败，检查网络或仓库权限</div>';}}
async function loadPostsForSearch(){if(allPostsCache.length>0){renderSearchResults(allPostsCache);return;}try{const res=await axios({url:`https://api.github.com/repos/${CONFIG.githubUsername}/${CONFIG.repoName}/contents/`,method:'GET',headers:{Accept:'application/vnd.github.v3+json'}});const md=res.data.filter(f=>f.name.endsWith('.md'));const list=await Promise.all(md.map(async f=>{const d=await axios({url:f.url,method:'GET',headers:{Accept:'application/vnd.github.v3+json'}});return {id:f.sha,title:f.name.replace('.md',''),created_at:d.data.created_at,download_url:f.download_url};}));list.sort((a,b)=>new Date(b.created_at)-new Date(a.created_at));allPostsCache=list;renderSearchResults(list);}catch(err){document.getElementById('searchResults').innerHTML='<div class="empty-state">加载失败</div>';}}
async function loadDetail(sha){document.getElementById('detailTitle').textContent='加载中...';document.getElementById('detailMeta').innerHTML='';document.getElementById('detailContent').textContent='';try{const p=allPostsCache.find(x=>x.id===sha);if(!p)throw new Error('文章不存在');const c=await axios.get(p.download_url);document.getElementById('detailTitle').textContent=p.title;document.getElementById('detailMeta').innerHTML=`<span>👤 ${CONFIG.githubUsername}</span><span>🕐 ${new Date(p.created_at).toLocaleString('zh-CN')}</span>`;document.getElementById('detailContent').innerHTML=marked.parse(c.data);}catch(err){document.getElementById('detailTitle').textContent='加载失败';document.getElementById('detailContent').textContent=err.message;}}
async function handleCreate(){const t=document.getElementById('createTitle').value.trim();const c=document.getElementById('createContent').value.trim();const err=document.getElementById('createError');const tk=getToken();if(!t||!c){err.textContent='标题和内容不能为空';return;}if(!tk){err.textContent='请先填写GitHub Token';checkTokenAndShowCreate();return;}err.textContent='';try{const fn=t.replace(/[\\/:*?"<>|]/g,'_')+'.md';const b64=btoa(unescape(encodeURIComponent(c)));await axios({url:`https://api.github.com/repos/${CONFIG.githubUsername}/${CONFIG.repoName}/contents/${fn}`,method:'PUT',headers:{Authorization:`token ${tk}`,Accept:'application/vnd.github.v3+json'},data:{message:`Add article: ${t}`,content:b64,branch:CONFIG.branch}});document.getElementById('createTitle').value='';document.getElementById('createContent').value='';alert('发布成功！');showPage('home');}catch(e){err.textContent=e.response?.data?.message||'发布失败，检查Token权限';}}
function filterPosts(){const k=document.getElementById('searchInput').value.trim().toLowerCase();if(!k){renderSearchResults(allPostsCache);return;}const f=allPostsCache.filter(p=>p.title.toLowerCase().includes(k));renderSearchResults(f);}
function renderSearchResults(list){const box=document.getElementById('searchResults');if(!list.length){box.innerHTML='<div class="empty-state">没有匹配文章</div>';return;}box.innerHTML=list.map(p=>`<div class="search-result-item" onclick="showPage('detail','${p.id}')"><span class="title">${escapeHtml(p.title)}</span><span class="date">${formatDate(p.created_at)}</span></div>`).join('');}
document.addEventListener('DOMContentLoaded',()=>{loadPosts();const icon=document.querySelector('link[rel="icon"]');if(icon)icon.href=CONFIG.avatarUrl;});
</script>
</body>
</html>
