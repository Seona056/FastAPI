from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()     # FastAPI 클래스 인스턴스

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)

# @app.get("/hello")      # 어노테이션: /hello라는 URL요청이 발생하면 해당 함수 리턴
# def hello():
#     return {"message":"안녕하세요 파이보"}

app.include_router(question_router.router)