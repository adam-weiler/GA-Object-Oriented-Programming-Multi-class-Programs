from products import Product

class Shopping_Cart():
    def __init__(self, name):
        self.name = name
        self.products = []

    def __str__(self): #Returns a meaningful string that describes the instance.
        return f'Shopping_Cart instance:name={self.name} products={self.products}'

    def add_to_cart(self, product):

        #add quantity to item.

        self.products.append(product)
        return f'{product.name} added to cart!'

    def remove_from_cart(self, product):
        if product in self.products:
            self.products.remove(product)
            return f'{product.name} removed from cart!'
        else:
            return 'That item isn\'t in your cart.'



    def most_expensive_product_in_cart(self):
        most_expensive_item = ''
        most_expensive_item_price = 0

        for product in self.products:

            if product.base_price > most_expensive_item_price:
                most_expensive_item = product
                most_expensive_item_price = product.base_price

        if most_expensive_item_price > 0:
            return f'The most expensive item is the {most_expensive_item.name} at ${most_expensive_item.base_price}.'
        else:
            return f'Your cart is empty.'


    

    def display_cart(self):
        for product in self.products:
            print(f'-{product.name} : ${product.base_price}')

    def calculate_total_before_tax(self):
        price = 0
        
        for product in self.products:
            price += product.base_price

        return price

    def calculate_total_tax(self):
        tax = 0

        for product in self.products:
            tax += product.calculate_tax()

        return tax

    def calculate_total_after_tax(self):
        return self.calculate_total_before_tax() + self.calculate_total_tax()

    def display_total(self):
        print(f'{self.name}\'s cart:')
        self.display_cart()
        print()

        price = self.calculate_total_before_tax()
        tax = self.calculate_total_tax()
        total = self.calculate_total_after_tax()

        print('Subtotal: ${:,.2f}'.format(price))
        print('Taxes: +${:,.2f}'.format(tax))
        
        print('TOTAL: ${:,.2f}'.format(total))









#Instantiate each Product class.
computer = Product('Computer', 1500, .15)
television = Product('Television', 2500, .20)
oculus_rift = Product('Oculus Rift', 999, .14)
iPhone = Product('Apple iPhone', 800, .13)


# #Instantiate each Shopping_Cart class.
# bobs_cart = Shopping_Cart('Bob')

# #Adding items to bobs_cart.
# print(bobs_cart.add_to_cart(computer))
# print(bobs_cart.add_to_cart(television))
# print(bobs_cart.add_to_cart(oculus_rift))
# print(bobs_cart.add_to_cart(iPhone))
# print()

# print(bobs_cart.most_expensive_product_in_cart())
# print()

# #Display all items in bobs_cart.
# bobs_cart.display_total()
# print('\n')


# #Instantiate each Shopping_Cart class.
# billys_cart = Shopping_Cart('Bob')

# #Adding items to billys_cart.
# print(billys_cart.add_to_cart(computer))
# print(billys_cart.add_to_cart(computer))
# print(billys_cart.add_to_cart(computer))
# print(billys_cart.add_to_cart(television))
# print(billys_cart.add_to_cart(oculus_rift))
# print(billys_cart.add_to_cart(iPhone))
# # print()

# print(billys_cart.remove_from_cart(television)) #Television removed.
# print(billys_cart.remove_from_cart(television)) #That item isn't in your cart.
# print(billys_cart.remove_from_cart(television))
# # print()

# print(billys_cart.most_expensive_product_in_cart())
# print()

# #Display all items in billys_cart.
# billys_cart.display_total()


#Instantiate each Shopping_Cart class.
carls_cart = Shopping_Cart('Carl')

print(carls_cart.most_expensive_product_in_cart()) #Your cart is empty.
print()

#Display all items in carls_cart.
carls_cart.display_total()