from fastapi import FastAPI, HTTPException

app = FastAPI()

USER_DB = {}

NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name Not Found.")

@app.post("/users/name/{name}/nickname/{nickname}")
def creat_user(name:str, nickname:str):
    USER_DB[name] = nickname
    return {"status": "success"}

@app.get("/users/name/{name}")
def read_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    return USER_DB[name]

@app.put("/users/name/{name}/nickname/{nickname}")
def update_user(name: str, nickname: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    USER_DB[name] = nickname
    return {"status": "success"}

@app.delete("/users/name/{name}")
def delete_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    del USER_DB[name]
    return {"status": "success"}