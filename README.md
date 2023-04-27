# 2-06 질문 상세

<br>

**프론트 엔드**
1. `Home.svelte` 파일 수정
2. `App.svelte` 파일 수정
3. `Detail.svelte` 파일 생성  

👉 [FastAPI 페이지](http://localhost:5173)에서 질문 목록 중 하나를 클릭하면, `http://localhost/#/detail/2`와 같은 URL이 호출  
👉 해당 질문의 아이디 값 `2`가 콘솔 브라우저에 출력되는 것을 확인

<br>

**백엔드**  
4. `question_crud.py` 파일 수정  
5. `question_router.py` 파일 수정  

👉 [FastAPI의 docs 문서](http://localhost:8000/docs)에서 새로만든 *질문 상세 조회 API*를 테스트
👉 `question_id`에 **2** 값을 입력하고 실행 ➡ 출력 확인

<br>

**프론트엔드**  
6. `Detail.svelte` 파일 수정

👉 [FastAPI 페이지](http://localhost:5173)에서 질문을 클릭하면 *질문 상세 조회 API*가 브라우저에 출력

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