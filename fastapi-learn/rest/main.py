from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def rest_root():
    return {'hello world'}


@app.get('/items/{item_id}')
def read_item(item_id, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
