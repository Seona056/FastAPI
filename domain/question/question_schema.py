import datetime

from pydantic import BaseModel


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
    
    class Config:
        orm_mode = True