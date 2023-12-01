# Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements.
# Input:
# t = [1, 2, 3, 4]
# output:
# [2, 3]

n = int(input("Enter the length "))
middle = []
print("Enter the element")
for i in range(n):
    ele = int(input())
    middle.append(ele)
middle.pop(n-1)
middle.pop(0)
# middle.remove()
print(middle)

