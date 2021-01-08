
from typing import Optional
from fastapi import Cookie, FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
# app = FastAPI()
# @app.post("/test/abc", response_model=schema.User,tags=["test"])
# def test():
#     return {"status":"OK"}

class Main(FastAPI):
    
    @self.post("/test/abc", response_model=schema.User,tags=["test"])
    def test():
        return {"status":"OK"}
    