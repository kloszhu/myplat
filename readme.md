## 依赖关系
### 生成依赖关系：
pip freeze > requirements.txt
### 还原依赖关系：
pip install -r requirements.txt
## 安装核心依赖
pip install fastapi
pip install uvicorn
## 启动
uvicorn main:app --reload
## CORS
origins = [
    "http://localhost:8000",
    "http://localhost:8000",
    "http://localhost:8000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
## 创建随机hash
openssl rand -hex 32
