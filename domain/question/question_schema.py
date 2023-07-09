import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer


# pydantic의 BaseModel을 상속한 Question 클래스를 "Question 스키마:라고 부른다.
# models.py의 Question 클래스는 "Question 모델"이라고 부른다.
class Question(BaseModel):
    '''
    id, subject, content, create_date 4개 항목 모두 디폴트값이 없기 때문에 "필수 항목"이다.
    
    👉 subject: int | None = None
    👉 subject는 int 또는 None을 가질 수 있고, 디폴트 값은 None
    '''
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []
    
    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용하지 않는다.')
        return v