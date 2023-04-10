# 질문 목록 라우터(question_router.py)를 그대로 옮긴 것 👉 이후 question_router.py 수정

from models import Question
from sqlalchemy.orm import Session


def get_question_list(db: Session):
    question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return question_list