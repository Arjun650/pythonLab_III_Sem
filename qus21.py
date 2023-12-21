# Create a comprehensive online shopping system with classes for Product, Customer, and Order. Implement features like adding products to the cart, placing orders, and calculating the total order amount. Consider discounts and promotions.

class Product:
    def __init__(self , productId , name , price):
        self.productId = productId
        self.name = name 
        self.price = price
    @staticmethod
    def addProduct( product , order):
        product.append(order)
    
class Customer:
    def __init__(self , customerId , customerName ):
        self.customerId = customerId
        self.customerName = customerName
        self.cart = []
    
    def addToCart(self , product ,  id ):
        for ob in product:
            if ob.productId == id:
                self.cart.append(ob)
    
    def viewCart(self):
        for ob in self.cart:
            print(ob.name , ob.price)

class Order:
    @staticmethod
    def calculateAmount( list ):
        total = 0 
        for ob in list:
            total += int(ob.price)
        return total
product = []
P1 = Product(1 , "pen ", "3")
P2 = Product(2, "watch  ", "323")
P3 = Product(3, "Phone ", "1300")
P4 = Product(4,"mouse ", "300")
P5 = Product(5, "Keyboard ", "1500")
P6 = Product(6, "Bike", "100300")

Product.addProduct(product , P1)
Product.addProduct(product , P2)
Product.addProduct(product , P3)
Product.addProduct(product , P4)
Product.addProduct(product , P5)
Product.addProduct(product , P6)

# for ob in product:
#     print(ob.name , ob.price)

cust1 = Customer(2332 , "Arjun")
cust1.addToCart(product , 1)
cust1.addToCart(product , 5)
cust1.addToCart(product , 6)
cust1.viewCart()
p = Order.calculateAmount(cust1.cart)
print(p)