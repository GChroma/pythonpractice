class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def total(self):
        sum = 0
        for x in self.items:
            sum += x.price*x.amount
        return sum