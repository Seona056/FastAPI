# 2-04 질문 목록 API 만들기

<br>

- **라우터(Router)** 👈
- 의존성 주입(Dependency Injection)
- Pydantic으로 하는 입출력 관리
- CRUD 파일 작성

<br>

## 2-04-1 라우터

<br>

1. `projects/myapi/domain/question` 디렉터리 생성
2. `question_router.py` 파일 생성
3. `main.py` 수정

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
