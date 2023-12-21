first = input("enter first number")
operator = input("enter the operator (+ , - , * , / , %)")
second= input("enter third number")

first = int(first)
second= int (second)

if( operator == "+"):
    print(first+second)
elif(operator == "-"):
    print(first-second)
elif(operator == "*"):
    print(first*second)
elif(operator == "/"):
    print(first/second)
elif(operator == "%"):
    print(first%second)
else:
    print("it is an invalid operator")