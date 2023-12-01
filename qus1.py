# 1.write a program to find sum of first n natural numbers.

n = input("Enter any number")
sum = 0 
for i in range(1 , int(n)+1):
    sum = sum+i

print("The sum of the n natural number of given number is " ,sum)