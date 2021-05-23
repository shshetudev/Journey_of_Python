"""
Statement:
1. Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.
2. If there are multiple students with the second lowest grade, order their names alphabetically
and print each name on a new line.
"""
from past.builtins import raw_input

score_list = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))