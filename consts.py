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

