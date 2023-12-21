# Create a program that performs various operations on a list, such as adding elements, removing duplicates, finding the maximum and minimum values, and calculating the average.

n = eval(input("Enter length of the list"))
def addElement(addE  , A):
    A.append(addE)

def removeDuplicate(A):
    a = 0 
    while ( a < len(A)):
        if ( (a+1) < len(A) ):
            if ( A[a] == A[a + 1]):
                a -= 1
                A.pop(a+1)
        a += 1
def maxMin(A):
    print (f"Max: {max(A)} \n Min: {min(A)}")

def calAvg(A):
    print(f"The average value of the list is {sum(A) / len(A)}")
A = []
print("enter elements of the list")
for i in range(n):
    
    ele = eval(input(f"enter element{i + 1}"))
    A.append(ele)

addElement(4 , A)
removeDuplicate(A)
maxMin(A)
calAvg(A)
print(A)