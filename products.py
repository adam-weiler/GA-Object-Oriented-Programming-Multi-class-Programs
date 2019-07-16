class Product():
    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def total_price(self):
        return self.base_price + (self.base_price * self.tax_rate)

computer = Product('Computer', 1500, .15)
# print(computer.name)

television = Product('Television', 2500, .20)
# print(television.name)

oculus_rift = Product('Oculus Rift', 999, .14)
# print(oculus_rift.name)

iPhone = Product('iPhone', 800, .13)
# print(iPhone.name)