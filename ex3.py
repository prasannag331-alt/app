class PaymentStrategy:
  def pay(self,amount):
    pass

class CreditCardPayment(PaymentStrategy):
  def pay(self,amount):
    print("Paid{amount} using credit card")

class PayPalPayment(PaymentStrategy):
  def pay(self,amount):
    print("paid {amount} using Paypal")

class Paymentcontext:
  def_init_(self,strategy):
  self.strategy = strategy

def set_strategy(self, strategy)"
self.strategy= strategy

def pay(self,amount):
  self.stratgy.pay(amount)
