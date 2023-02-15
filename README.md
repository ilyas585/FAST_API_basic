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
    
