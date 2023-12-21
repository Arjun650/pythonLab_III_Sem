class Person:
    def __init__(self , name , occ):
        self.name = name 
        self.occ = occ
    def printName(self):
        print(self.name)
        print(self.occ)

A = Person("Arjun" , "student")
A.printName()