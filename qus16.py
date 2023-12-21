# Build a program that performs operations on a dictionary, such as adding and removing key-value pairs, checking if a key exists, and iterating over the keys and values.

n = eval(input("enter total number of pairs"))

dict = {}

def addValue(dict , key , value):
    dict[key] = value
    # del dict[key]
def removeValue(dict , key):
    if key in dict:
        del dict[key]
def checkKey(dict , checkKey):
    for key , value in dict.items():
        if key == checkKey:
            print("exists")
for i in range(n):
    key = input("enter the key")
    value = input("enter the value")
    dict[key] = value
addValue(dict , 'd' , 3)
removeValue(dict , 'a')
checkKey(dict , 'b')

print(dict)