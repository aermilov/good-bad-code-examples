class InventoryManager:
    def __init__(self):
        self.items = {}
        self.log_actions = True

    def log(self, message):
        if self.log_actions:
            print(message)

    def add_item(self, item_name, quantity):
        self.log(f"Adding {quantity} of {item_name}.")
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        self.log(f"Added {quantity} of {item_name}.")

    def check_inventory(self, item_name):
        return self.items.get(item_name, 0)

    def remove_item(self, item_name, quantity):
        current_quantity = self.check_inventory(item_name)
        if current_quantity >= quantity:
            self.items[item_name] -= quantity
            self.log(f"Removed {quantity} of {item_name}.")
        else:
            self.log(f"Not enough {item_name} to remove. Requested: {quantity}, Available: {current_quantity}")

# Пример использования
inventory = InventoryManager()
inventory.add_item("apples", 50)
inventory.remove_item("apples", 10)
