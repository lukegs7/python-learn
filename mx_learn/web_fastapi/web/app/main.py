from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/')
def root():
    print(requests.__name__)
    return 'This is written by fastapi'
