def mx(fx):
    def fmx():
      print("good morning")
      fx()
      print("thank you ")
    return fmx
@mx
def hello():
   print("Hello World")

hello()