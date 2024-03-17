import uvicorn
from fastapi import FastAPI
from flask_pymongo import MongoClient

app = FastAPI()
MongoURL = "mongodb+srv://JayBhakhar:jay456789@schedulesamsmu.uczju06.mongodb.net/"

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)