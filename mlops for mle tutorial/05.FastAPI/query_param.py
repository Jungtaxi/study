from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name":"Foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]

# Query Parameter (items/?skip=0&limit=10)
# function parameter 로는 사용되지만 Path Operation 에 포함되지 않아 Path Parameter 라고 할 수 없는 parameter
@app.get("/items/")
def read_item(skip: int=0, limit: int= 10):
    return fake_items_db[skip : skip + limit]

# needy parameter (items/foo-item?needy=someneedy)
# 값을 입력 받아야하는 (기본 값이 없는), ? 뒤에 입력을 해 주어야 에러가 발생하지 않음
# @app.get("/items/{item_id}")
# def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item