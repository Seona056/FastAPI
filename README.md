# 2-02 모델로 데이터베이스 관리하기

<br>

1. ORM 라이브러리 설치하기

    ```
    pip install sqlalchemy
    ```
2. `database.py` 파일 생성
3. `models.py` 파일 생성
4. alembic 설치
    ```
    pip install alembic
    ```
5. alembic 초기화
    ```
    alembic init migrations
    ```
    5-1) `alembic.ini` 파일 수정
    ```
    (... 생략 ...)
    sqlalchemy.url = sqlite:///./myapi.db
    (... 생략 ...)
    ```
    5-2) `migrations` 디렉터리의 `env.py` 파일 수정
    ```
    (... 생략 ...)
    import models
    (... 생략 ...)
    target_metadata = models.Base.metadata
    (... 생략 ...)
    ```
6. 리비전 파일 생성
    ```
    alembic revision --autogenerate
    ```
7. 리비전 파일 실행
    ```
    alembic upgrade head
    ```
8. `.gitinore` 추가
