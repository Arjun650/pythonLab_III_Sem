# 1. Given a string, find the count of how many times each letter appears and store the result in a dictionary.

# a = {}
# c = 'a'
# b = 3 ;

# a[f"{c}"] = b

# print (a)

word = (input("Enter any string"))
def lettercount(word):
    dict = {}
    for c in word:
        if c.isalpha():
            count = word.count(c)
            dict[f"{c}"] = count
    return dict
dict1 = lettercount(word)
print(dict1)