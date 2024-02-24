class Vehicle:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def move(self):
        if self.type == "car":
            print("Driving a car")
        elif self.type == "airplane":
            print("Flying an airplane")

