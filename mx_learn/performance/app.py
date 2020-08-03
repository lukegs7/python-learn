import time
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def func():
    print('This is an api')
    return 'func'


@app.get('/name')
def func1():
    print('geshuai1992')
    time.sleep(10)
    return 'geshuai1992'


if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8080)
