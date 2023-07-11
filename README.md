# 2-09 부트스트랩으로 더 쉽게 화면 꾸미기

<br>

1. 부트스트랩 설치
    ```
    frontend % npm install bootstrap
    ```

2. `main.js`파일 수정 
    - `bootstrap.min.css`, `bootstap.min.js`파일을 임포트 한다.

3. `Home.svelte` 파일 수정
    - 부트스트랩 적용 테이블 생성
    - 기존 ul 태그는 삭제

4. `Detail.svelte` 파일 수정
    - 질문 상세 화면에서 부트스트랩 적용 테이블 생성
    - 기존 ul 태그는 삭제

5. `Error.svelte` 파일 수정
    - 오류 컴포넌트에 부트스트랩 적용



<br>

# 2-10 질문 등록

<br>

**백엔드**  

1. `question_schema.py` 파일 수정
    - **QuestionCreate** 스키마 생성

2. `question_crud.py` 파일 수정
    - **create_question** 함수 정의

3. `question_router.py` 파일 수정
    - 라우터 함수 **question_create** 정의

- http://localhost:8000/docs#/ 에서 작성한 API가 정상 작동하는지 확인해보자.  
- 테스트를 해 보면 204 상태코드가 리턴된다면 정상

<br>

**프론트엔드**  

4. `Home.svelte` 파일 수정
    - **질문 등록하기**버튼 생성  

5. `App.svelte` 파일 수정
    - **QustionCreate 컴포넌트**를 등록 (페이지 경로 추가) 

6. `QuestionCreate.svelte` 파일 생성

- http://localhost:5174/에서 **질문 등록하기**버튼이 추가된 것을 확인

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