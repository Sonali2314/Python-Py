'''
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
'''

import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    c=['student_id','age']
    df=pd.DataFrame(student_data,columns=c)
    return df

student_data=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]]
df=createDataframe(student_data)
print(df)
