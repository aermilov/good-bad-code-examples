class InventoryManager:
    def __init__(self):
        self.items = {}
        self.log_actions = True

    def add_item(self, item_name, quantity):
        if self.log_actions:
            print(f"Adding {quantity} of {item_name}.")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        if self.log_actions:
            print(f"Added {quantity} of {item_name}.")

    def check_inventory(self, item_name):
        if self.log_actions:
            print(f"Checking inventory for {item_name}.")
        if item_name in self.items:
            print(f"Inventory has {self.items[item_name]} of {item_name}.")
            return True
        else:
            print(f"{item_name} is not in inventory.")
            return False

    def remove_item(self, item_name, quantity):
        if self.log_actions:
            print(f"Trying to remove {quantity} of {item_name}.")
        if self.check_inventory(item_name):
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.log_actions:
                    print(f"Removed {quantity} of {item_name}.")
            else:
                print(f"Not enough {item_name} to remove. Requested: {quantity}, Available: {self.items[item_name]}")
        else:
            print(f"Cannot remove {item_name} because it is not in the inventory.")

    # Дополнительный метод, который, возможно, никогда не будет использоваться.
    def log_inventory(self):
        if self.log_actions:
            for item_name, quantity in self.items.items():
                print(f"Inventory: {item_name} has {quantity} items.")

# Пример использования
inventory = InventoryManager()
inventory.add_item("apples", 50)
inventory.remove_item("apples", 10)
inventory.log_inventory()