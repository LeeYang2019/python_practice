import datetime
myTimeNow = datetime.datetime.now()
myTimeNowText = "the time now is "
print(myTimeNowText, myTimeNow)

x = 10
y = "10"
z = 10.5

sum1 = x + x
sum2 = y + y
sum3 = x + z

student_grades = [2, 3, 5, 6]

mySum = sum(student_grades)
myMax = max(student_grades)
length = len(student_grades)
mean = mySum / length

myReverse = reversed(student_grades)
print(mean)
print(myMax)
print(myReverse)

newStudent_Grades = {"marry": 9.1, "sim": 8.8, "John": 7.5}
print(newStudent_Grades.values())
print(sum(newStudent_Grades.values()))

myList = [{"marry": 25, "student": True}, {"john": 25, "student": False}]

dataTuple = (1, 2, 3)
list(dataTuple)

print(dataTuple)

listData = [1, 2, 3]
tuple(listData)

print(listData)

newList = [["name", "john"], ["surname", "johnson"]]
dict(newList)

print(newList)

newTmpList = [1,4,5,8,7,5]

