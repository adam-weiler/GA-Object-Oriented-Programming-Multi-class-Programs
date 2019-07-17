from products import Product
from shopping_cart import Shopping_Cart

#Instantiate each Product class.
computer = Product('Computer', 1500, .15)
television = Product('Television', 2500, .20)
oculus_rift = Product('Oculus Rift', 999, .14)
iPhone = Product('Apple iPhone', 800, .13)
# print(computer.name)
# print(television.name)
# print(oculus_rift.name)
# print(iPhone.name)

#Instantiate each Shopping_Cart class.
bobs_cart = Shopping_Cart('Bob')

#Adding items to bobs_cart.
print(bobs_cart.add_to_cart(computer))
print(bobs_cart.add_to_cart(television))
print(bobs_cart.add_to_cart(oculus_rift))
print(bobs_cart.add_to_cart(iPhone))
print()

#Display all items in bobs_cart.
bobs_cart.display_total()
print('\n')


#Instantiate each Shopping_Cart class.
billys_cart = Shopping_Cart('Bob')

#Adding items to billys_cart.
print(billys_cart.add_to_cart(computer))
print(billys_cart.add_to_cart(computer))
print(billys_cart.add_to_cart(computer))
print(billys_cart.add_to_cart(television))
print(billys_cart.add_to_cart(oculus_rift))
print(billys_cart.add_to_cart(iPhone))
print()

print(billys_cart.remove_from_cart(television))
print(billys_cart.remove_from_cart(television))
print(billys_cart.remove_from_cart(television))
print()

#Display all items in billys_cart.
billys_cart.display_total()