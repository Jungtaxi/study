from fastapi import FastAPI

app = FastAPI()

# path parameter
# Path Operation 에 포함된 변수로 사용자에게 입력받아 function 의 argument 로 사용되는 parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}