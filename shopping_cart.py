from products import Product

class Shopping_Cart():
    def __init__(self, name):
        self.name = name
        self.products = []
        print(f'{self.name}\'s Shopping Cart:')

    def __str__(self): #Returns a meaningful string that describes the instance.
        return f'{self.name}\'s Shopping Cart has these products: {self.products}'

    def add_to_cart(self, product, quantity):
        if quantity >= 1:
            for num in range(1, quantity+1):
                self.products.append(product)
            return f'{product.name} x {quantity} added to cart!'
        else:
            return 'You cannot buy less than 1 product.'

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