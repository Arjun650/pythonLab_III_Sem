n = int(input("Enter the size of the array"))
def sumElement(arr):
    return sum(arr)
arr = []
for i in range(n):
    element = int(input("Enter the element"))
    arr.append(element)
summm = sumElement(arr)
print(summm)