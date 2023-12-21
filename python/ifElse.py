a  = int(input("Enter any number"))

if (a == 0):
    print("It is zero")
elif( a %2 == 0):
    print("It is an even number")
    if(a > 0):
        print("it is greater than zero")
else:
    print("It is an odd number")