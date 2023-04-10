# 2-04 질문 목록 API 만들기

<br>

- 라우터
- 의존성 주입(Dependency Injection)
- **Pydantic으로 하는 입출력 관리** 👈
- CRUD 파일 작성

<br>

## 2-04-3 스키마

<br>

1. **Pydantic이란?**  
    FastAPI의 입출력 스펙을 정의하고 그 값을 검증하기 위해 사용하는 라이브러리. FastAPI 설치 시 함께 설치된다.
2. `domain/question` 디렉터리에 `question_schema.py` 파일 생성
3. `question_router.py` 수정 👉 라우터에 Pydantic 적용

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