n = int(input("enter length of array"))
def maximum(arr):
    return max(arr)
arr = []
print("Enter elements")
for i in range(n):
    element = int(input())
    arr.append(element)

maxx = maximum(arr)
print(maxx)