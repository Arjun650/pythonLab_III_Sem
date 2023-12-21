# Create a program that filters a list of strings based on a given condition, such as selecting only words that start with a specific letter or have a certain length.

list = ["apple", "giraffe", "ocean", "mountain", "python", "breeze", "coffee", "keyboard", "umbrella", "whisper", "firefly", "octopus", "moonlight", "carousel","arjun" , "harmony"
]

newList = []

def newListSearch(list , newList , searchLetter):
    for a in list:
        if a.startswith(searchLetter):
            newList.append(a)

newListSearch(list , newList , 'a')
print(newList)