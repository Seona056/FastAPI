# 2-05 질문 목록 화면 만들기

<br>

- 질문 목록 화면 구현하기
- **라우터 컴포넌트** 👈
- API 호출 라이브러리

<br>

## 2-05-2 스벨트 라우터

<br>

1. svelte-spa-router 설치하기  
    1-1) 터미널에서 실행중인 svelte 서버를 중지시킨다. 👉 cmd창에서 `ctrl + c`  
    1-2) svelte-spa-router 설치
    ```
    frontend % npm install svelte-spa-router
    ```
2. `frontend/src`안에 `routes` 디렉터리 생성
3. `Home.svelte` 파일 생성
4. `App.svelte` 파일 수정

<br>

### 질문 목록 확인

<br>

- http://localhost:5173 를 브라우저에서 실행한다.

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