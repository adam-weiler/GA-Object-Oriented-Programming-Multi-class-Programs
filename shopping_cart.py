from products import Product

class Shopping_Cart():
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)
        return f'{product.name} added to cart!'

    def remove_from_cart(self, product):
        if (product in self.products):
            self.products.remove(product)
            return f'{product.name} removed from cart!'
        else:
            return 'That item isn\'t in your cart.' 

    def display_cart(self):
        for product in self.products:
            print(f'-{product.name} - ${product.base_price} - {product.tax_rate}%')

        # return self.products






computer = Product('Computer', 1500, .15)
# print(computer.name)

television = Product('Television', 2500, .20)
# print(television.name)

oculus_rift = Product('Oculus Rift', 999, .14)
# print(oculus_rift.name)

iPhone = Product('Apple iPhone', 800, .13)
# print(iPhone.name)



bobs_cart = Shopping_Cart()
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

bobs_cart.display_cart()


# computer = Product('Computer', 1500, .15)
# print(computer.name)


#Shopping cart
#Add total cost of all products in cart (before tax)
#Add total cost of all products in cart (after tax)

