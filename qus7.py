# Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise.
# Input:
# is_sorted([1, 2, 2])
# Output:
# True
# Input:
# is_sorted(['b', 'a'])
# output:
# False

n = eval(input("Enter the lenght of list"))
myList = []

def isSorted(l):
    for j in range(len(l)):
        if myList[j] > myList[j+1]:
            return False
        else:
            return True

for i in range(n ):
    ele = eval(input("Enter number"))
    myList.append(ele)
print(isSorted(myList))