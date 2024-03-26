import uvicorn
from fastapi import FastAPI
from flask_pymongo import MongoClient
import pandas as pd
import uuid
import consts

app = FastAPI()
MongoURL = "mongodb+srv://JayBhakhar:jay456789@schedulesamsmu.uczju06.mongodb.net/"
SchduleSaMSMUCollection = MongoClient(MongoURL).datadase.SchduleSaMSMU
GroupCollection = MongoClient(MongoURL).datadase.GroupSAMSMU

def addData():
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

'''
arguments of get requst
groupID - str, week - int
'''

@app.get("/")
# def Schudule(group_name, week):
def Schudule():     
    # date_time = 0
    searchquery = consts.SearchQuery(week = 0)
    print(searchquery)
    output = []
    for schdule in SchduleSaMSMUCollection.find({"groupID": 301, "date_time": searchquery}):    
        output.append(schdule)   
    """
    output: list return of schdule of one week of group
    """
    return {'Schdule': output}

"""
arguments of get requst
facultID- int

"""

@app.get("/groupList")
def Group(facultID):
    output = []
    for group in GroupCollection.find({"facultID": facultID}):
        output.append(group)
    """
    output: [{1:"301"}, {2:"302"}, {3:"303"}]
    """
    return {'group_list': output}


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)

