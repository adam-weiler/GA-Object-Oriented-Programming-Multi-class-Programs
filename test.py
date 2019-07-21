from products import Product
from shopping_cart import Shopping_Cart

#Instantiate each Product class.
computer = Product('Computer', 1500, 'standard')
television = Product('Television', 2500, 'standard')
oculus_rift = Product('Oculus Rift', 999, 'imported')
iPhone = Product('Apple iPhone', 800, 'imported')
mouse_pad = Product('Mouse Pad', 5, 'tax-exempt')



#Instantiate each Shopping_Cart class.
bobs_cart = Shopping_Cart('Bob')

#Adding items to cart.
print(bobs_cart.add_to_cart(computer, 1))
print(bobs_cart.add_to_cart(television, 1))
print(bobs_cart.add_to_cart(oculus_rift, 1))
print(bobs_cart.add_to_cart(iPhone, 3))
print(bobs_cart.add_to_cart(mouse_pad, 1))
print()

print(bobs_cart.most_expensive_product_in_cart())
print()

#Display all items in bobs_cart.
bobs_cart.display_total()
print('\n\n')



#Instantiate each Shopping_Cart class.
billys_cart = Shopping_Cart('Billy')

#Adding items to cart.
print(billys_cart.add_to_cart(computer, 1))
print(billys_cart.add_to_cart(computer, 1))
print(billys_cart.add_to_cart(computer, 1))
print(billys_cart.add_to_cart(television, 1))
print(billys_cart.add_to_cart(oculus_rift, 3))
print()

print(billys_cart.remove_from_cart(television)) #Television removed.
print(billys_cart.remove_from_cart(television)) #That item isn't in your cart.
print(billys_cart.remove_from_cart(television))
print(billys_cart.remove_from_cart(iPhone)) #That item isn't in your cart
print()

print(billys_cart.most_expensive_product_in_cart())
print()

#Display all items in billys_cart.
billys_cart.display_total()
print('\n\n')



#Instantiate each Shopping_Cart class.
carls_cart = Shopping_Cart('Carl')

#Adding items to cart.
print(carls_cart.add_to_cart(computer, -1))
print()

print(carls_cart.remove_from_cart(television)) #That item isn't in your cart.
print()

print(carls_cart.most_expensive_product_in_cart()) #Your cart is empty.
print()

#Display all items in carls_cart.
carls_cart.display_total()