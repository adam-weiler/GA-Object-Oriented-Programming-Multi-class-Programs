class Product(): #A Product class.
    def __init__(self, name, base_price, tax_rate): #Every Product has attributes name, base_price, and tax_rate.
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    # def total_price(self):
    #     return self.base_price + (self.base_price * self.tax_rate)

    # def calculate_price_before_tax(self):

        # price = 0
        
        # for product in self.products:
            # price += product.base_price
        # price

        # return price


    def calculate_tax(self):
        tax = self.base_price * self.tax_rate

        return tax

    
    def calculate_price_after_tax(self):
        price = round((self.base_price + self.calculate_tax()),2)

        # for product in self.products:
        #     price += product.base_price * product.tax_rate

        return price 

# computer = Product('Computer', 1500, .15)
# print(computer.name)

# television = Product('Television', 2500, .20)
# print(television.name)

# oculus_rift = Product('Oculus Rift', 999, .14)
# print(oculus_rift.name)

# iPhone = Product('iPhone', 800, .13)
# print(iPhone.name)