import uvicorn
from fastapi import FastAPI
from flask_pymongo import MongoClient
import pandas as pd
import uuid
from datetime import date, datetime

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
db.collection.find({
    day: {
        $gt: ISODate("2020-01-21"),
        $lt: ISODate("2020-01-24")
    }
})'group_name':301,
groupID - str, week - int
'''

@app.get("/")
# def Schudule(group_name, week):
def Schudule():
    week = 0
    if week == 0:
        print(date.today().weekday())
        startYear, startMonth, startDay = date.today().year, date.today().month, date.today().day + 6
        startDate = datetime(startYear, startMonth, startDay)
    """
    convert week int to date
    function which will return week schdule by week int
    """
    date_time = 0
    output = []
    # for schdule in SchduleSaMSMUCollection.find({"groupID": groupID, "date_time": date_time}):
    for schdule in SchduleSaMSMUCollection.find({'group_name':301,'date': startDate}):
        output.append(schdule)
    """
    output: list return of schdule of one week of group
    """
    # print(output[0])
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

