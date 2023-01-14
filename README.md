## FAST API 

#### request
- Path ```validation params of url```
- Query ```validation params of query```
- Body ```validation params of request body```
- Field ```validation field of request body```
- @validator ```validation field of request body (additional checkers)```

#### response
- response_model  ```parameter in endpoint, for check response```
- response_model_exclude ```exclude fields in response```
- response_model_include ```include fields in response```
- from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse


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
