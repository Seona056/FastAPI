from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db     # from database import SessionLocal에서 SessionLocal 객체를 반환하는 get_db로 변경
from domain.question import question_schema     # question_schema.py 파일 생성 후 추가
from models import Question

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])     # question_schema.py 파일 생성 후 response_model 추가 👉 config 클래스에서 orm_mode = True 설정 후 Question 스키마로 자동 매핑된다.
def question_list(db: Session = Depends(get_db)):
    '''
    1️⃣ 첫 번째 실습 코드
    form database import SessionLocal
    
    def question_list():
        db = SessionLocal()
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
        db.close()
        return _question_list
    
    2️⃣ 두 번째 실습 코드
    
    from database import get_db 
    
    def question_list():
        with get_db() as db:
            _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
        return _question_list
    
    👉 get_db 함수를 with구문으로 불러오면 with구문이 끝나면 자동으로 db.close()가 실행됨
    
    3️⃣ 세 번째 실습 코드 : 현재 작성된 fastapi의 depends를 사용한 코드 
    
    👉 with구문이 삭제되면서 database.py의 @contextlib.contextmanager 어노테이션을 삭제한다.
    '''
    
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()     # 최신글부터 정렬 (역순)
    
    return _question_list
    
