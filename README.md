# 2-07 답변 등록

<br>

**백엔드**  

1. `answer` 디렉토리를 생성하고 `answer_router.py`, `answer_crud.py`, `answer_schema.py` 파일 생성
2. `main.py` 파일 수정

<br>

**프론트엔드**  

3. `api.js` 파일 수정
4. `Detail.svelte` 파일 수정

<br>

**백엔드**

5. `answer_schema.py` 파일 수정
6. `question_schema.py` 파일 수정

<br>

**프론트엔드**

7. `frontend/src/components` 디렉토리에 `Error.svelte` 파일을 생성

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