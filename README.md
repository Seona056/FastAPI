# 2-04 질문 목록 API 만들기

<br>

- 라우터
- **의존성 주입(Dependency Injection)** 👈
- Pydantic으로 하는 입출력 관리
- CRUD 파일 작성

<br>

## 2-04-2 의존성 주입

<br>

1. 데이터베이스 세션의 생성과 반환을 자동화 
2. 의존성 주입  

> `database.py`, `question_router.py` 코드 수정 (3가지 버전 공부 ✔3️⃣ 최종적용)

||`database.py`|`question_router.py`|
|:---:|:---|:---|
|1️⃣|`get_db()` 함수 선언|`from database import get_db`|
|2️⃣|- `@contextlib.contextmanager`어노테이션<br>- `try-finally` 예외처리 구문|with 구문으로 자동화|
|3️⃣|어노테이션 삭제 (필수)|- fastapi의 Depends 사용|

<br>

### 질문 목록 API 테스트

<br>

- http://localhost:8000/docs 를 브라우저에서 실행한다.

<br>

**<위의 링크를 실행하기 전>**

1. FastAPI 서버를 실행 (Uvicorn) : 백엔드 서버
    ```
    (myapi) myapi % uvicorn main:app --reload
    ```
2. Svelte 서버를 실행 : 프론트엔드 서버
    ```
    frontend % npm run dev
    ```