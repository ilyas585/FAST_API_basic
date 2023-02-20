## FAST API 

#### request
- Path ```validation params of url```
- Query ```validation params of query```
- Body ```validation params of request body```
- Field ```validation field of request body```
- @validator ```validation field of request/response body (additional checkers)```

- APIRouter 
```
  create group of endpoints, indicate prefix and tags
  add to main app for work
  - from fastapi import APIRouter
  - app.include_router(router_product)
```

#### response
- response_model  ```parameter in endpoint, for check response```
- response_model_exclude ```exclude fields in response```
- response_model_include ```include fields in response```
- from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
- from fastapi import HTTPException ```raise exception for response (usually errors)```

#### product
- crud.py - functions for endpoints products group
- views.py - bind endpoints and functions products group
- schemas.py - all models of products group
- helper.py - additional functions and classes for products group

### other Python modules
- Typing [List, Dict, Set etc.]```validation additional data types```



## uvicorn

- uvicorn main:app --reload
- uvicorn main:app --reload --port 80  =>  http://127.0.0.1/docs
- uvicorn main:app --reload --port 8000 --host 0.0.0.0

```
run server with reload

for install uvicorn pip install uvicorn
```

#### venv - virtual environment
- base python3.8(or python3.9) without libraries
- pip install flask/ pydantic/ uvicorn etc... all requrements

#### gitignore
- specifying files and folders that cannot be added to github
    - venv
    - sqlite3

#### requrements.txt
- specifying requirement libraries
- for collect requirements ```pip freeze > requirements.txt```
    - fastapi
    - sqlalchemy
    - uvicorn
    - pydantic
    
# Docker version 19.03.1
- deploy - развернуть приложение
- собрать зависимости и запустить приложение - Docker
- depends: OS, python, libraries, external(db, other service etc.)

- command for docker:
  - ```docker images``` - посмотреть список уставновленных docker-образов
  - ```docker run python:3.9-alpine``` - run docker-image (if first time, download it)
  - ```docker run python:3.9-alpine -h 0.0.0.0 -p 8000:8000``` run docker-image with arguments: h=0.0.0.0, p=8000:8000
  - ```docker ps -a```  - see all docker-containers
  - ```docker stop 14c5d9385025``` and ```docker rm 14c5d9385025``` stop and remove docker-container
  - ```docker rmi b908778bd1b0``` - remove docker-image by id
  - ```docker build . -t python-6-fastapi-basic``` - create image by Dockerfile
  - ```docker run -p 80:80 python-6-fastapi-basic``` - run my application FAST API
  - ```docker run -p 80:80 -it python-6-fastapi-basic``` - run container, enter terminal in container
  - ```docker run -p 80:80 -d python-6-fastapi-basic``` - run container in daemon
  - ```docker exec -it 14c5d9385025 /bin/bash``` - enter ti container in terminal
  - ```docker logs -f 14c5d9385025``` - see logs in container
  

- command for dockerfile:
  - pip install -r requirements.txt
  - COPY
  - CMD
  - FROM


