import time
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def func():
    return 'func'


@app.get('/name')
async def func1():
    return 'geshuai1992'

# if __name__ == '__main__':
#     uvicorn.run('app:app', host='localhost', port=8080)
