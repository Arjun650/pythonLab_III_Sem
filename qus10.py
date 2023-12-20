# Given a list of numbers, write a Python program to find the second largest number in the given list.

n = eval(input("enter length of list"))
myList = []

def secondLargest(myList):
    myList.sort()
    print(myList[-2])

for i in range(n):
    ele = input()
    myList.append(ele)

secondLargest(myList)