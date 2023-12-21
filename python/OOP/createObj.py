class Person:
    name = ""
    RegistrationNo = ""
    classs = ""
    def display(self):
        print(f"Name: {self.name}")
        print(f"Registration No :{self.RegistrationNo}")
        print(f"Class : {self.classs}")

A = Person()
A.name = "Arjun"
A.RegistrationNo = "Bl.en.u4cse22186"
A.classs = 'CSEB'
A.display()
# print(A.name , A.RegistrationNo , A.classs)