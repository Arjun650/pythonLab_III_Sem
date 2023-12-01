# Write a function called list_add that takes a list of lists of integers and adds up the elements from all of the nested lists.

n = int(input("Enter the length of the list"))

L = []
list1 = []
list2 = []
print("enter the elements")
for i in range (n):
    ele = int(input())
    L.append(ele)
for i in range (n ):
    if(L[i] % 2 == 0 ):
        list1.append(L[i])
    else:
        list2.append(L[i])

print("even: " , list1)
print("Odd" , list2)