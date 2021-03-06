from fastapi import FastAPI

app = FastAPI()


@app.get('/{id}')
def func(id):
    return f"8000:{id}"


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('demo:app', port=8000)
