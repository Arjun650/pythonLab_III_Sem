# 3.Write a python program to check if a particular element is present in list.

sizeList  = int(input("Enter the size of the list"))

myList = []

for i in range(sizeList):
    element = int(input("Enter the element"))
    myList.append(element)

# print(myList)
# for i in range(sizeList):
#     print(myList[i])
searchElement = int(input("Enter the search Element"))

if searchElement in myList:
    loc = myList.index(searchElement)
    print("Element found at " , loc + 1)
else:
    print("Element not Found !!!")

