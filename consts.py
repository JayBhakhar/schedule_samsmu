from datetime import date, datetime

faculty_dic = {}
""" 
using dict for facultyId and Name | to get requst for groupList
"""
"""
group collection
_id: uuid - str
facultyID -  int
faculty_name - str 
groupList - dict {groupID: groupName}

schdule collection
_id: uuid - str
date: Isodate
time: int
subject_name - str
group_name - str
address - str
teacher_name - str
room_no - str
type - str
"""


facultyList = [
  'Лечебное дело',
  'Педиатрия',
  'Стоматология',
  'Медико-профилактическое дело',
  'Фармация',
  'Клиническая Психология',
  'Медицинская Кибернетика',
  'Сестринское Дело',
  'General Medicine',
  'Dentistry',
  'Pharmacy'
  ],

for i in range(len(facultyList)):
    faculty_dic[i] = facultyList[i]

def SearchQuery(week):
    startDate = 0
    endDate = 0
    if week == 0:   
      year, month, day = date.today().year, date.today().month, date.today().day 
      startWeek = date.today().weekday()+1 % day
      try:
        # TODO:convert week int to date(INT)
      except ValueError:
          return ValueError
    return {"$gte": startDate, "$lte": endDate}

        
        
