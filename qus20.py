# Create a simple inventory system with classes for Product and Inventory. The Product class should have attributes like product ID, name, and price. The Inventory class should manage a list of products with methods for adding, removing, and displaying products.

class Product:
    def __init__(self , ProductId , name , price):
        self.ProductId = ProductId
        self.name = name 
        self.price = price


class Inventory:
    # def __init__(self ):
        
    def adding(self , list , P1):
        list.append(P1)
    def removing(self , list , key):
        for ob in list:
            if ob.ProductId == key:
                list.remove(ob)
    def display(self , list):
        for ob in list:
            print(ob.name , ob.price)
            print('--' * 5)

list = []
inventory = Inventory()

P1 = Product(1 , "pen" , "$5")
P2 = Product(2 , "watch " , "$30")
P3 = Product(3 , "mobile" , "$1300")
P4 = Product(4 , "Honey" , "$100")
inventory.adding(list , P1)
inventory.adding(list , P2)
inventory.adding(list , P3)
inventory.adding(list , P4)
inventory.removing(list, 2)
inventory.display(list)



