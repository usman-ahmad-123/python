from fastapi import FastAPI
import json
app = FastAPI()
def load_data():
    with open()

@app.get("/")
def hello():
    return {'message': 'Hello world'}

@app.get("/about")
def about():
    return {'message': 'Campus is an education platform'}
