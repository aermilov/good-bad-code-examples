class Dish:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

class Order:
    def __init__(self, dishes, table_number):
        self.dishes = dishes
        self.table_number = table_number

class RestaurantManagementSystem:
    def __init__(self):
        self.orders = []

    def create_order(self, dishes, table_number):
        order = Order(dishes, table_number)
        self.orders.append(order)
