import uvicorn
from fastapi import FastAPI
from flask_pymongo import MongoClient
import pandas as pd
import uuid
import consts

app = FastAPI()
MongoURL = DATABASE_LINK
SchduleSaMSMUCollection = MongoClient(MongoURL).datadase.SchduleSaMSMU
GroupCollection = MongoClient(MongoURL).datadase.GroupSAMSMU

def addSchdule():
    data = pd.read_excel(r'schdule.xlsx')
    # TODO: merge data and time
    df = data[['date','time','subject_name','group_name','address','teacher_name','room_no','type']]
    df['_id'] = 0
    for i in range(len(df['_id'])):
        df.loc[i, '_id'] = str(uuid.uuid4())
    df = df.where(pd.notnull(df), None)
    df.replace({pd.NaT: None})
    results = df.to_dict(orient="records")
    SchduleSaMSMUCollection.insert_many(results)

def addGroup():    
    GroupCollection.find_one_and_update(
        {
            '_id':2,
        },
        { "$set":
          {
            'Педиатрия': "['1st year'],['2nd year'],['3rd year'],['4th year'],['5th year'],['6th year']"
          } 
        }
    )

@app.get("/")
def Schudule():
    searchquery = consts.SearchQuery(week = 0)
    output = []
    for schdule in SchduleSaMSMUCollection.find({"group_name": 301, "date": searchquery}):
        output.append(schdule)
    return {'Schdule': output}


@app.get("/groupList")
def Group(id):
    output = []
    for group in GroupCollection.find({"_id": int(id)}):
        output.append(group)   
    return {'group_list': output}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
