# mlops for mle Tutorial

## Reference

**해당 폴더는 아래의 사이트의 학습 튜토리얼을 따라갑니다.**

https://mlops-for-mle.github.io/tutorial/docs/intro

**Kimdongui, mlops-for-mle Tutorial, (2013), GitHub repository,** 

https://github.com/mlops-for-mle/tutorial

## Environment

- Ubuntu 20.04

## DataBase

<aside>

### DB Server Creation
#### 목표[](https://mlops-for-mle.github.io/tutorial/docs/database/db-server-creation#%EB%AA%A9%ED%91%9C)

1. Docker 를 이용하여 DB 서버를 생성합니다.
2. 생성된 DB 의 role name 과 attributes 를 확인합니다.

#### 스펙 명세서[](https://mlops-for-mle.github.io/tutorial/docs/database/db-server-creation#%EC%8A%A4%ED%8E%99-%EB%AA%85%EC%84%B8%EC%84%9C)

1. Docker 를 설치합니다.
2. PostgreSQL DB 서버를 생성합니다.
    - Image : `postgres:14.0`
    - Container name : `postgres-server`
    - POSTGRES_USER : `myuser`
    - POSTGRES_PASSWORD : `mypassword`
    - POSTGRES_DB : `mydatabase`
    - Port forwarding : `5432:5432`
3. 생성된 DB 서버를 확인합니다.
    - `psql` 로 DB 에 접근하여 role name 과 attributes 확인
</aside>

<aside>

### 💡 **Table Creation**

#### 목표[](https://mlops-for-mle.github.io/tutorial/docs/database/table-creation#%EB%AA%A9%ED%91%9C)

1. 생성된 DB 에 query 를 작성하여 테이블을 생성합니다.
2. 생성된 테이블을 확인합니다.

#### 스펙 명세서[](https://mlops-for-mle.github.io/tutorial/docs/database/table-creation#%EC%8A%A4%ED%8E%99-%EB%AA%85%EC%84%B8%EC%84%9C)

1. `pandas`, `psycopg2-binary`, `scikit-learn` 패키지를 설치합니다.
2. Python 스크립트를 이용하여 DB 에 접근합니다.
    - user : `myuser`
    - password : `mypassword`
    - host : `localhost`
    - port : `5432`
    - database : `mydatabase`
3. `psycopg2` 패키지를 사용하여  테이블을 생성합니다.
    
    `iris_data`
    
    - 테이블은 다음과 같은 column 들을 갖고 있어야 합니다.
        
        
        | column | id | sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | target |
        | --- | --- | --- | --- | --- | --- | --- |
        | type | primary key | float | float | float | float | int |
4. `psql` 을 이용하여 생성한 테이블을 확인합니다.

</aside>

<aside>

### 💡 **Data Insertion**

#### 목표[](https://mlops-for-mle.github.io/tutorial/docs/database/data-insertion#%EB%AA%A9%ED%91%9C)

1. 생성한 테이블에 iris 데이터 한 줄을 삽입합니다.
2. 삽입한 데이터를 확인합니다.

#### 스펙 명세서[](https://mlops-for-mle.github.io/tutorial/docs/database/data-insertion#%EC%8A%A4%ED%8E%99-%EB%AA%85%EC%84%B8%EC%84%9C)

1. Python 스크립트를 이용하여 DB 에 접속합니다.
    - user : `myuser`
    - password : `mypassword`
    - host : `localhost`
    - port : `5432`
    - database : `mydatabase`
2. `psycopg2` 패키지를 이용하여 생성된 `iris_data` 테이블에 데이터 row 1개를 삽입합니다.
3. `psql` 을 이용하여 삽입한 데이터를 확인합니다.
</aside>

<aside>

### 💡 **Data Insertion Loop**

#### 목표[](https://mlops-for-mle.github.io/tutorial/docs/database/data-insertion-loop#%EB%AA%A9%ED%91%9C)

1. 생성된 테이블 안에 데이터를 계속해서 생성하는 스크립트를 작성합니다.
2. DB 에 데이터가 계속해서 삽입되고 있는지 확인합니다.

#### 스펙 명세서[](https://mlops-for-mle.github.io/tutorial/docs/database/data-insertion-loop#%EC%8A%A4%ED%8E%99-%EB%AA%85%EC%84%B8%EC%84%9C)

1. 3) Data Insertion 챕터에서 작성한 스크립트를 이용하여 계속해서 데이터를 생성하는 스크립트를 작성합니다.
2. 생성된 `iris_data` 테이블에 `psycopg2` 를 이용하여 스크립트를 실행해 계속해서 데이터를 삽입합니다.
3. `psql` 을 이용하여 삽입되고 있는 데이터를 확인합니다.
</aside>

<aside>

### 💡 **Data Generator on Docker**

#### 목표[](https://mlops-for-mle.github.io/tutorial/docs/database/data-generator-docker#%EB%AA%A9%ED%91%9C)

1. 앞서 작성했던 코드를 Docker 컨테이너 안에서 실행하기 위해 Dockerfile 을 작성합니다.
2. Docker 컨테이너 간의 네트워크를 연결하여 DB 에 데이터를 계속해서 삽입합니다.
3. DB 안에 데이터가 계속해서 삽입되고 있는지 확인합니다.

#### 스펙 명세서[](https://mlops-for-mle.github.io/tutorial/docs/database/data-generator-docker#%EC%8A%A4%ED%8E%99-%EB%AA%85%EC%84%B8%EC%84%9C)

1. 4) Data Insertion Loop 챕터에서 작성한 스크립트를 build 할 수 있는 Dockerfile 을 작성합니다.
    - Base image 는 `amd64/python:3.9-slim` 을 사용합니다.
    - 컨테이너에서 `psql` 을 이용하여 DB 에 접속할 수 있도록 `postgresql-client` 를 설치합니다.
    - 컨테이너에서 코드가 실행될 수 있도록 `scikit-learn`, `pandas`, `psycopg2-binary` 을 설치합니다.
    - 4) Data Insertion Loop 챕터에서 작성한 스크립트를 복사합니다.
    - `ENTRYPOINT` 와 `CMD` 를 이용하여 스크립트를 실행합니다.
2. Dockerfile 을 이용하여 이미지를 build 하고 실행합니다.
3. Docker Network 를 통해 컨테이너 간의 네트워크를 연결하여 DB 에 데이터를 계속해서 삽입합니다.
    - `docker network create` 명령어를 이용하여 `my-network` 라는 네트워크를 생성합니다.
    - `docker network connect` 명령어를 이용하여 생성한 `my-network` 에 postgres server 를 연결합니다.
    - Build 된 이미지를 다시 실행합니다. 이때 `-network` 옵션을 이용하여 `my-network` 네트워크에 연결합니다.
4. `psql` 을 이용하여 DB 에 데이터가 계속해서 쌓이고 있는지 확인합니다.
</aside>

<aside>

### 💡 **Data Generator on Docker Compose**

#### 목표[](https://mlops-for-mle.github.io/tutorial/docs/database/data-generator-docker-compose#%EB%AA%A9%ED%91%9C)

1. DB 컨테이너와 Data Generator 컨테이너를 함께 띄우기 위한 Docker Compose 파일을 작성합니다.
2. DB 안에 데이터가 계속해서 삽입되고 있는지 확인합니다.

#### 스펙 명세서[](https://mlops-for-mle.github.io/tutorial/docs/database/data-generator-docker-compose#%EC%8A%A4%ED%8E%99-%EB%AA%85%EC%84%B8%EC%84%9C)

1. Docker Compose 파일을 작성합니다.
    - Postgres Server
        - Service name : `postgres-server`
        - Image : `postgres:14.0`
        - Container name : `postgres-server`
        - Environment
            - POSTGRES_USER : `myuser`
            - POSTGRES_PASSWORD : `mypassword`
            - POSTGRES_DB : `mydatabase`
        - Port forwarding : `5432:5432`
    - Data Generator
        - Service name : `data-generator`
        - Image : `Dockerfile`
        - Container name : `data-generator`
        - Command : `["postgres-server"]`
    
    INFO
    
    Postgres Server 서비스와 Data Generator 서비스를 띄울 때 어떤 서비스가 먼저 생성되어야 하는지 생각해보고, 그 기능을 Compose 파일에 추가합니다.
    
2. Docker Compose 파일을 실행합니다.
3. `psql` 을 이용하여 DB 에 데이터가 계속해서 쌓이고 있는지 확인합니다.
    - Local 에서 확인합니다.
    - Data Generator server 에서 확인합니다.
</aside>