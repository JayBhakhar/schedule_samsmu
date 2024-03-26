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


facultyList = ['Лечебное дело',
  'Педиатрия',
  'Стоматология',
  'Медико-профилактическое дело',
  'Фармация',
  'Клиническая Психология',
  'Медицинская Кибернетика',
  'Сестринское Дело',
  'General Medicine',
  'Dentistry',
  'Pharmacy'],

for i in range(len(facultyList)):
    faculty_dic[i] = facultyList[i]

def SearchQuery(week):
    startDate = 0
    endDate = 0
    if week == 0:      
      year, month, day = date.today().year, date.today().month, date.today().day     
      startWeek = date.today().weekday()+1 
      try:
          if year == 2024:
            if date.today().month == 4:
              if startWeek == 1:
                if day == 29 :
                  startDate = datetime(year, month, day)
                  endDate = datetime(year, month+1, 4)
                else:                    
                  startDate = datetime(year, month, day)
                  endDate = datetime(year, month, day+5)                    
              elif startWeek == 2:
                if day == 30:
                    startDate = datetime(year, month, day-1)
                    endDate = datetime(year, month+1, 4)
                else:                    
                    startDate = datetime(year, month, day-1)
                    endDate = datetime(year, month, day+4)
              elif startWeek == 3:
                startDate = datetime(year, month, day-2)
                endDate = datetime(year, month, day+3)
              elif startWeek == 4:
                startDate = datetime(year, month, day-3)
                endDate = datetime(year, month, day+2)
              elif startWeek == 5:
                startDate = datetime(year, month, day-4)
                endDate = datetime(year, month, day+1)
              elif startWeek == 6:
                startDate = datetime(year, month, day-5)
                endDate = datetime(year, month, day)
              elif startWeek == 7:
                if day == 28 :
                  startDate = datetime(year, month, day+1)
                  endDate = datetime(year, month+1, 4)
                else:
                  startDate = datetime(year, month, day+1)
                  endDate = datetime(year, month, day+6)
            elif date.today().month == 5:
              if startWeek == 1:
                if day == 27 :
                  startDate = datetime(year, month, day)
                  endDate = datetime(year, month+1, 1)
                else:                    
                  startDate = datetime(year, month, day)
                  endDate = datetime(year, month, day+5)
              elif startWeek == 2:
                if day == 28:
                  startDate = datetime(year, month, day-1)
                  endDate = datetime(year, month+1, 1)
                else:                    
                  startDate = datetime(year, month, day-1)
                  endDate = datetime(year, month, day+4)
              elif startWeek == 3:
                if day == 29:
                  startDate = datetime(year, month, day-2)
                  endDate = datetime(year, month+1, 1)
                elif day == 1:
                  startDate = datetime(year, month-1, 29)
                  endDate = datetime(year, month, day+3)                      
                else:                    
                  startDate = datetime(year, month, day-2)
                  endDate = datetime(year, month, day+3)
              elif startWeek == 4:
                if day == 30:
                  startDate = datetime(year, month, day-3)
                  endDate = datetime(year, month+1, 1)
                elif day == 2:
                  startDate = datetime(year, month-1, 29)
                  endDate = datetime(year, month, day+2) 
                else:                    
                  startDate = datetime(year, month, day-3)
                  endDate = datetime(year, month, day+2)
              elif startWeek == 5:
                if day == 31:
                  startDate = datetime(year, month, day-4)
                  endDate = datetime(year, month+1, 1)
                elif day == 3:
                  startDate = datetime(year, month-1, 29)
                  endDate = datetime(year, month, day+1) 
                else:                    
                  startDate = datetime(year, month, day-4)
                  endDate = datetime(year, month, day+1)
              elif startWeek == 6:
                if day == 4:
                  startDate = datetime(year, month-1, 29)
                  endDate = datetime(year, month, day) 
                else:                    
                  startDate = datetime(year, month, day-5)
                  endDate = datetime(year, month, day)
              elif startWeek == 7:
                if day == 26 :
                  startDate = datetime(year, month, day+1)
                  endDate = datetime(year, month+1, 1)
                else:
                  startDate = datetime(year, month, day+1)
                  endDate = datetime(year, month, day+6)
            elif date.today().month == 6:
              if startWeek == 1:                
                startDate = datetime(year, month, day)
                endDate = datetime(year, month, day+5)
              elif startWeek == 2:
                startDate = datetime(year, month, day-1)
                endDate = datetime(year, month, day+4)
              elif startWeek == 3:       
                startDate = datetime(year, month, day-2)
                endDate = datetime(year, month, day+3)
              elif startWeek == 4:       
                startDate = datetime(year, month, day-3)
                endDate = datetime(year, month, day+2)
              elif startWeek == 5:       
                startDate = datetime(year, month, day-4)
                endDate = datetime(year, month, day+1)
              elif startWeek == 6:
                if day == 1:
                  startDate = datetime(year, month-1, 27)
                  endDate = datetime(year, month, day) 
                else:                    
                  startDate = datetime(year, month, day-5)
                  endDate = datetime(year, month, day)
              elif startWeek == 7:
                if day == 30 :
                  startDate = datetime(year, month, day+1)
                  endDate = datetime(year, month+1, 6)
                else:
                  startDate = datetime(year, month, day+1)
                  endDate = datetime(year, month, day+6)
      except ValueError:
          return ValueError
    return {"$gte": startDate, "$lte": endDate}

    """
    convert week int to date
    function which will return week schdule by week int
    """
        
        