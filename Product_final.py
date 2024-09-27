# Maintainer: Attia Inayat (SP23-BAI-012)
# Collaborator: Noor Fatima (SP23-BAI-046)
class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price
    
  def get_price(self, quantity):
      if quantity<0:
          raise ValueError('Quantity is not valid')
      elif quantity<10: # for 0 to 9
          discount = 0
      elif quantity<100: # for 10 to 99
          discount = 0.10
      else: # for 100 or above
          discount = 0.20

      totalprice= quantity * self.price * (1 - discount)
      return totalprice
  
  def make_purchase(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot purchase a negative quantity")
        
        if quantity > self.amount:
            raise ValueError(f"Cannot purchase {quantity} items, only {self.amount} in stock.")
        
        # Get price with any applicable discount
        total_price = self.get_price(quantity)
        
        # Reduce stock by the purchased amount
        self.amount -= quantity
        
        # Display the total price charged
        print(f"Purchased {quantity} {self.name}(s) for ${total_price:.2f}. Stock remaining: {self.amount}.")
  


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






