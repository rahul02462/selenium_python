import pandas as pd

# array = {
#       'name' : ['Rahul','harsha','sudhir'],
#       'age' : [27,28,30]
# }
#
# myVar = pd.DataFrame(array)
# print(myVar)

list = [
      ['rahul',28,'Software Engineer'],
      ['Harsh',27,'Automation QA'],
      ['Sudhir',26,'Software Enginner']
]

myVar = pd.DataFrame(list,columns=['Name','Age','Designation'])
print(myVar)