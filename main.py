from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "Welcome"}


@app.get("/exercises")
def get_all_exercises():
    return {"exercises": ["Bench Press", "Shoulder Press", "Deadlift", "Chest Fly"]}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

