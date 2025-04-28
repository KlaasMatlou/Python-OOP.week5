# Design Your Own Class -  Superhero: Tanjiro Kamado


# Base class representing a Demon Slayer
class DemonSlayer:
    def __init__(self, name, corps_rank):
        self.name = name
        self.demon_slayer_corps_rank = corps_rank
        self.number_of_slain_demons = 0

    def get_demon_slayer_info(self):
        return f"Name: {self.name}, Corps Rank: {self.demon_slayer_corps_rank}, Demons Slain: {self.number_of_slain_demons}"

    def slay_demon(self, demon_name):
        self.number_of_slain_demons += 1
        print(f"{self.name} has slain the demon: {demon_name}!")

# Subclass representing Tanjiro Kamado, inheriting from DemonSlayer
class Tanjiro(DemonSlayer):
    def __init__(self, corps_rank):
        super().__init__("Tanjiro Kamado", corps_rank)
        self.breathing_style = "Water Breathing"
        self.nichirin_sword_color = "Black"
        self.total_concentration_constant = False
        self.current_health = 100
        self.is_injured = False

    def perform_breathing_technique(self, technique_name):
        print(f"{self.name} performs {self.breathing_style}: {technique_name}!")

    def achieve_total_concentration(self):
        self.total_concentration_constant = True
        print(f"{self.name} has achieved Total Concentration!")

    def take_damage(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0
            self.is_injured = True
            print(f"{self.name} has taken {amount} damage and is severely injured!")
        elif self.current_health < 30:
            self.is_injured = True
            print(f"{self.name} has taken {amount} damage and is injured.")
        else:
            print(f"{self.name} has taken {amount} damage.")

# Method to get a comprehensive overview of Tanjiro's current status
    def get_info(self):
        return f"{super().get_demon_slayer_info()}, Breathing Style: {self.breathing_style}, Sword Color: {self.nichirin_sword_color}, Health: {self.current_health}, Injured: {self.is_injured}, Total Concentration: {self.total_concentration_constant}"

# Example usage
tanjiro = Tanjiro("Kanoe")
print(tanjiro.get_info())
tanjiro.perform_breathing_technique("Second Form - Water Wheel")
tanjiro.take_damage(40)
print(tanjiro.get_info())
tanjiro.slay_demon("Lower Moon Five")
print(tanjiro.get_demon_slayer_info())



# Activity 2: Polymorphism Challenge!

class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} makes a generic movement.")

class Dog(Animal):
    def move(self):
        print(f"{self.name} runs on four legs.")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flies through the air.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swims in the water.")

class Snake(Animal):
    def move(self):
        print(f"{self.name} slithers on the ground.")

# Demonstrate Polymorphism
animals = [
    Dog("Buddy"),
    Bird("Tweety"),
    Fish("Nemo"),
    Snake("Kaa"),
]

print("Demonstrating Polymorphism:")
for animal in animals:
    animal.move()