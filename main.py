from fastapi import FastAPI,Path

app = FastAPI()

#app是FaskApi实例,get是请求方法,请求路径
@app.get("/")               #装饰器
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def get_hello():
    return {"message":"hello"}

@app.get("/book/{id}")
async def get_book(id:int):
    return {"message":id,"title":f"book int {id}"}

@app.get("/book/{id}")
async def get_book(id=Path(...,gt=0,lt=101)):
    return {"message":id,"title":f"book int {id}"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
