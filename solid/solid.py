from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving a car")

class Airplane(Vehicle):
    def move(self):
        print("Flying an airplane")
