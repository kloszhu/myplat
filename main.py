# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from typing import Optional

from fastapi import Cookie, FastAPI,APIRouter
from dao.usercontroller import router as userrouter
from fastapi.middleware.cors import CORSMiddleware
# from jwtauth import router
from dao.usercontroller import router as userdaorouter

app = FastAPI()

# 路由
app.include_router(userrouter)
app.include_router(userdaorouter)
# CORS
origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000",
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


