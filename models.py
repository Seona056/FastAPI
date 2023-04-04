from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True)  # 기본 키로 설정 : 중복 없는 고유값
    subject = Column(String, nullable=False)    # null값 허용하지 않음
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    

class Answer(Base):
    __tablename__ = "answer"
    
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))    # Question() 클래스에서 생성된 테이블 question의 컬럼 id와 연결된다.
    question = relationship("Question", backref="answers")      # backref : 역참조