# Given a list, write a Python program to swap first and last element of the list.

n = int(input("Enter the length of the list"))
myList = []
def letSwap(myList):
    temp = myList[0]
    myList[0] = myList[-1]
    myList[-1] = temp

for i in range(n):
    ele = eval(input())
    myList.append(ele)

letSwap(myList)
for j in myList:
    print (j)
