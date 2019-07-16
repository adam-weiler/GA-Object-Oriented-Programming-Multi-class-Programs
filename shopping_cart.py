from products import Product

class Shopping_Cart():
    def __init__(self):
        self.products = []

    def add_to_cart(self):
        self.products.append(Product('Hamster', 10, .50))






computer = Product('Computer', 1500, .15)
# print(computer.name)

television = Product('Television', 2500, .20)
# print(television.name)

oculus_rift = Product('Oculus Rift', 999, .14)
# print(oculus_rift.name)

iPhone = Product('iPhone', 800, .13)
# print(iPhone.name)



bobs_cart = Shopping_Cart()
bobs_cart.add_to_cart()
bobs_cart.add_to_cart()
bobs_cart.add_to_cart()
print(bobs_cart.products[0].name)
print(bobs_cart.products[0].base_price)
print(bobs_cart.products[0].tax_rate)

# computer = Product('Computer', 1500, .15)
# print(computer.name)


#Shopping cart
#Add a product to cart
#Remove a product from cart
#Add total cost of all products in cart (before tax)
#Add total cost of all products in cart (after tax)

