# grading.py
score = int(input("Please enter the assignment, test, or quiz score: > "))
valid = 1
if score >100:
    valid = 0
    print("erroneous input")
grade_sign = ''
if score % 10 > 7:
    grade_sign = '+'
if score % 10 < 3:
    grade_sign = '-'
if score >=90 and score <=100 and valid == 1:
    grade = 'A'
if score >=80 and score <=89 and valid == 1:
    grade = 'B'
if score >=70 and score <=79 and valid == 1:
    grade = 'C'
if score >=60 and score <=69 and valid == 1:
    grade = 'D'
if score <60 and valid == 1:
    grade = "F"
if valid == 1:
    print("The grade is "+grade+grade_sign)
