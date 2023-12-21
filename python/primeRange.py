a  = int(input("Enter the lower range"))
b = int(input("Enter the upper range"))

for i in range(a , b+1):
    count = 0 
    for j in range(1 , i+  1):
        if(i % j == 0):
            count = count + 1 
    if(count == 2 ):
        print(i)
        