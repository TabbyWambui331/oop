# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with their own move() behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴‍♀️")

# Using polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()
