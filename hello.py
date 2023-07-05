from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/items/5?q=somequery
# item_id will be 5, and q will be 'somequery'


@app.get("/items/{item_id}")
# typing.Union 类型用来表示一个变量可能拥有多种类型之一的情况。， q可以是str或者None，q的默认值是None，表示q是可选参数
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 查询参数默认值
fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]

# http://localhost:8000/list/ = http://localhost:8000/list/?skip=0&limit=10


@app.get("/list/")
async def read(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# 可选参数，默认值设置为 None 来声明可选查询参数


@app.get("/options/{item_id}")
async def options(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# 多路径参数


@app.get("/users/{user_id}/product/{product_id}")
async def get_user(user_id: str, product_id: str, q: str = None, short: bool = False):
    item = {"user_id": user_id, "product_id": product_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing product that has a long description"})
    return item
