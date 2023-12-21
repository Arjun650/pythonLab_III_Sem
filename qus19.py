# Create a simple inventory system with classes for Product and Inventory. The Product class should have attributes like product ID, name, and price. The Inventory class should manage a list of products with methods for adding, removing, and displaying products.

class Product:
    def __init__(self , productID , name , price ):
        self.productID = productID
        self.name = name
        self.price = price

# class Inventory:
#     def __init__(self ):
#         self.product = []
#     def adding(self , P1 , product):
#         self.product.append(P1)
         


    # def removing(self):
    
    # def displayProduct(self):

things = []

P1 = Product(1 , 'pen' , '300$')
P2 = Product(2 , 'mouse' , '23$')
P3 = Product(3 , 'keyboard' , '200$')
P4 = Product(4 , 'watch' , '30$')
things.append(P1)
things.append(P2)
things.append(P3)
things.append(P4)


# inventory = Inventory()

for a in things:
    print(a.productID , a.name , a.price)