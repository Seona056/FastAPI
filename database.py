# import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# @contextlib.contextmanager    # question_router.py에서 with구문 대신 fastapi의 depends를 사용해서 session객체 사용
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:            # 예외처리 구문 중 finally는 에러가 나더라도 무조건 실행된다.
        db.close()