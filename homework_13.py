#### 13.1. Очистити текст від html-тегів ####
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    cleaned = re.sub(r"<[^>]+>", "", html)

    lines = cleaned.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    result = "\n".join(non_empty_lines)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(result)

delete_html_tags("draft.html")

#### 13.2. Корзина для покупок ####
class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, count):
        self.products[item] = count

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {count} pcs." for item, count in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self):
        return sum(item.price * count for item, count in self.products.items())

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
