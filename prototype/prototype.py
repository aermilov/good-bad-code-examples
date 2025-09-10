import copy


class DishPrototype:
    def clone(self):
        return copy.deepcopy(self)

class Dish(DishPrototype):
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
        self.dish_prototypes = {}

    def add_dish_prototype(self, dish):
        self.dish_prototypes[dish.name] = dish

    def create_order(self, dishes, table_number):
        dishes = [self.dish_prototypes[name].clone() for name in dish_names]
        order = Order(dishes, table_number)
        self.orders.append(order)
