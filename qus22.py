# Design a program that uses a dictionary to store information about students. Each student should have a unique student ID as the key, and the values should include the student's name, age, and grades. Implement methods to add a new student, retrieve student information, and calculate the average grade for a student.

n = eval(input("enter total number of student"))

stuDetail = {}
stuDatabase  ={}


for i in range(n):
    id = eval(input("enter id"))
    name = input("enter your name")
    age = eval(input("enter your age"))
    grade = eval(input("enter grade"))
    stuDetail = {'name':name , 'age' : age , 'grade' : grade}
    stuDatabase[id] = stuDetail 

print(stuDetail)

print(stuDatabase)