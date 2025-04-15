# Base class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power   # Encapsulated attribute
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, protector of {self.city}!")

    def use_power(self):
        print(f"{self.name} uses {self._power}!")

# Subclass: FlyingSuperhero inherits from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Polymorphism: override use_power
    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h using {self._power}!")

# Creating objects
hero1 = Superhero("AquaBolt", "Water Manipulation", "Atlantis")
hero2 = FlyingSuperhero("SkyWing", "Wind Control", "Sky City", 900)

# Calling methods
hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()
