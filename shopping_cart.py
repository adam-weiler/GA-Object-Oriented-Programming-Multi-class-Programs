from products import Product

class Shopping_Cart():
    def __init__(self, name):
        self.name = name
        self.products = []

    def __str__(self): #Returns a meaninful string that describes the instance.
        return f'Shopping_Cart instance:name={self.name} products={self.products}'


    def add_to_cart(self, product):
        self.products.append(product)
        return f'{product.name} added to cart!'


    def remove_from_cart(self, product):
        if (product in self.products):
            self.products.remove(product)
            return f'{product.name} removed from cart!'
        else:
            return 'That item isn\'t in your cart.' 


    # def calculate_price_before_tax(self):
    #     price = 0
        
    #     for product in self.products:
    #         price += product.base_price

    #     return price


    # def calculate_tax(self):
    #     tax = 0

    #     for product in self.products:
    #         tax += product.base_price * product.tax_rate

    #     return tax


    def display_cart(self):
        for product in self.products:
            print(f'-{product.name} - ${product.base_price} - {product.tax_rate}% -- {product.calculate_tax()} - {product.calculate_price_after_tax()}')


    def calculate_price_after_tax(self):
        price = self.calculate_price_before_tax() + self.calculate_tax()

        # for product in self.products:
        #     price += product.base_price * product.tax_rate

        return price


    def display_price(self):
        print(f'{self.name}\'s cart:')
        self.display_cart()
        print()

        # price = self.calculate_price_before_tax()
        # tax = self.calculate_tax()
        # total = self.calculate_price_after_tax()

        # print('Cost of items: ${:,.2f}'.format(price))
        # print('Cost of taxes: +${:,.2f}'.format(tax))
        
        # print('TOTAL: ${:,.2f}'.format(total))




computer = Product('Computer', 1500, .15)
# print(computer.name)

television = Product('Television', 2500, .20)
# print(television.name)

oculus_rift = Product('Oculus Rift', 999, .14)
# print(oculus_rift.name)

iPhone = Product('Apple iPhone', 800, .13)
# print(iPhone.name)



bobs_cart = Shopping_Cart('Bob')
# print(bobs_cart)
print(bobs_cart.add_to_cart(computer))
print(bobs_cart.add_to_cart(computer))
print(bobs_cart.add_to_cart(television))
print(bobs_cart.add_to_cart(oculus_rift))
print(bobs_cart.add_to_cart(iPhone))
print()

print(bobs_cart.remove_from_cart(television))
print(bobs_cart.remove_from_cart(television))
print()

# print(bobs_cart.products[0].name)
# print(bobs_cart.products[0].base_price)
# print(bobs_cart.products[0].tax_rate)



# print(bobs_cart.calculate_price_before_tax())
# print(bobs_cart.calculate_price_after_tax())
bobs_cart.display_price()


# computer = Product('Computer', 1500, .15)
# print(computer.name)


#Shopping cart
#Add total cost of all products in cart (before tax)
#Add total cost of all products in cart (after tax)