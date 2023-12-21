a = int(input("Enter any number"))
b = a 
def isPalindrome(a):
    rev = 0 
    while a>0:
        rem = a %10 ; 
        rev = int(rev) *10 + int(rem) 
        a  = a //10
    return rev

if b == isPalindrome(a):
    print("It is a palindrome ")
else:
    print("It is not a palindrome")