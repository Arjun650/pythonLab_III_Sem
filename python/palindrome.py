a = int(input("Enter any number"))
b = a
rev = 0 
while a>0:
    rem = a %10 ; 
    rev = int(rev) *10 + int(rem) 
    a  = a //10

print(rev)
if rev == b:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")