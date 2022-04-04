class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age): # First param is always 'self'.
        self.name = name
        self.age = age
        
    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {car.color} car has {car.mileage:,} miles."
        
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass
