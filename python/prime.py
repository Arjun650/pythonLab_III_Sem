a = int(input("Enter any number"))

for x in range(1 , a+1):
    count = int(0) ; 
    for y in range(1 , int(x)+1):
        if( x % y == 0):
            count += 1
    if count == 2:
        print(x)