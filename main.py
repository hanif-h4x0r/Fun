import os
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running!"}
   
@app.get("/users/{user_id}")
def read_user(user_id: int, q: str | None = None):
    return {"user_id": user_id, "q": q}
    