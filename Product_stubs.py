class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price
    
  def get_price(self, quantity):
      pass
  
  def make_purchase(self, quantity):
      pass


laptop =Product('laptop',100,1000)
#Value error case
try:
    
    laptop.make_purchase(-2)  

except:
    print('Value Error: '+ ValueError)


# for 0 to 9
try:
    laptop.make_purchase(6)  

except:
    print('Value Error: '+ ValueError)

# for 10 to 99
try:
    laptop.make_purchase(59)  

except:
    print('Value Error: '+ ValueError)

# for 100 or above 
try:
    laptop.make_purchase(600)  

except:
    print('Value Error: '+ ValueError)





