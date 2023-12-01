# Write a function called list_add that takes a list of lists of integers and adds up the elements from all of the nested lists.
# Sample Input:
# t = [[1, 2], [3], [4, 5, 6]]
# output:
# 21

t = [[1 , 2] , [3] , [4 , 5, 6 ] , [3 , 4 , 6 , 7]]
sum = 0 
def addList(t):
    global sum
    for i in t:
        for j in i:
            sum = sum + j


addList(t)
print(sum)