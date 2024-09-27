import app

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
