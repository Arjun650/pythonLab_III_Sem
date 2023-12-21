n = int(input("Enter length of array"))
def swapping(arr ):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
arr = []

for i in range(n):
    ele = int(input())
    arr.append(ele)

swapping(arr)

print(arr)