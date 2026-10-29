#Pandas Series
#1. Creating Pandas Series:
import pandas as pd
marks = [95, 92, 89, 85, 80]
Custom_index = ['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
marks = pd.Series(marks, index=Custom_index)
# 2. Indexing and Slicing 
print("Marks for Rank1:", marks['Rank1'])
print("Marks for Rank2:", marks['Rank2'])
print("Marks for Rank3:", marks['Rank3'])
marks_first_rank = marks.iloc[0]
print("1st Rank Student Mark",marks_first_rank)
top3_ranks = marks.loc['Rank1':'Rank3']
print(" Top 3 ranks" ,top3_ranks)
third_rank = marks.iloc[2]
print("third rank student Marks" ,third_rank)
highscores = marks[marks > 90]
print("High scores (marks > 90):\n", highscores)
print()
#3. Manipulating Series:
marks['Rank1'] = 100
marks=marks.drop('Rank5')
print("Updated Marks:\n", marks)
print()
cgpa_marks = marks / 10
print("CGPA Marks:\n", cgpa_marks)
