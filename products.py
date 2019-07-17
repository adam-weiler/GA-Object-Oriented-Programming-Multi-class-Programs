class Product(): #A Product class.
    def __init__(self, name, base_price, tax_rate): #Every Product has attributes name, base_price, and tax_rate.
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def calculate_tax(self):
        return self.base_price * self.tax_rate
    
    def calculate_price_after_tax(self):
        return round((self.base_price + self.calculate_tax()),2)