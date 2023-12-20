# 3. Write a python code to create a dictionary and if a value in the dictionary is given print its key.

n = eval(input("enter the number of sets you want to enter"))
dict1 = {}
def getdata(dict1 , n):
    for i in range(n):
        value = (input("enter the value of the dictonary"))
        key = eval(input("enter the key of the value"))
        dict1[f"{value}"] = key

getdata(dict1 , n)

searchElement = input("enter the searchelment")

if searchElement in dict1:
    print(f"{searchElement} : {dict1[searchElement]}")
else:
    print("Search element not found")
# print(dict1)