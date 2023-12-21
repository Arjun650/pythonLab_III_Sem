import random
a = random.randrange(1 , 100 , 1)

guessed = 0 ; 
while(a != guessed):
    guessed = int(input("Enter the guessed number"))
    if(a == guessed):
        print("You are correct")
    elif(guessed < a + 10 ):
        print("low")
    else:
        print("high")