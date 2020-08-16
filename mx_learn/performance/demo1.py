from fastapi import FastAPI

app = FastAPI()


@app.get('/{id}')
def func(id):
    return f"8001:{id}"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('demo1:app', port=8001)
