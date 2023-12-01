# .write a program that prints the following pyramid on the screen.The number of lines must be obtained from the user input.
# 1
# 2 2
# 3 3 3
# 4 4 4 4

n = input("Enter the number of rows")

for i in range (1 , int(n)+1):
    for j in range(1 , int(i)+1):
        print(i , end ="")
    print("")