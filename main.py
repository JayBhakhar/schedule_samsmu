import uvicorn
from fastapi import FastAPI
from flask_pymongo import MongoClient
import pandas as pd
import uuid

app = FastAPI()
MongoURL = "mongodb+srv://JayBhakhar:jay456789@schedulesamsmu.uczju06.mongodb.net/"
SchduleSaMSMUCollection = MongoClient(MongoURL).datadase.SchduleSaMSMU

def addData():
    data = pd.read_excel(r'Book1.xlsx')
    df = data[['Date','Time','Subject_name','Group_name','Address','Teacher_name','Room_no','type']] 
    df['_id'] = 0
    print(df['Date'])
    for i in range(len(df['_id'])):
        df.loc[i, '_id'] = str(uuid.uuid4())
    df = df.where(pd.notnull(df), None)
    df.replace({pd.NaT: None})
    results = df.to_dict(orient="records")
    SchduleSaMSMUCollection.insert_many(results)

@app.get("/")
def read_root():
    output = []
    for supplier in SchduleSaMSMUCollection.find():
        output.append(supplier)
    return {'Schdule': output}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)