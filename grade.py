marks = input ("Enter Your Marks : ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B+"
elif marks >= 40:
    grade = "C+"
elif marks >= 33:
    grade = "D+"
elif marks >= 0:
    grade = "F"
print (grade)
    
