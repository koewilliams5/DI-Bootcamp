# Exercise 1 : Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1 : Create Siamese class
class Siamese(Cat):
    pass

# Step 2 : Create cat instances
cat1 = Bengal("Blèse", 12)
cat2 = Chartreux("Binja", 2)
cat3 = Siamese("Youpi", 7)

all_cats = [cat1, cat2, cat3]

# Step 3 : Create Pets instance
sara_pets = Pets(all_cats)

# Step 4 : Take cats for a walk
sara_pets.walk()








# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight!"
        else:
            return f"{other_dog.name} won the fight!"


# Step 2: Create dog instances
dog1 = Dog("Rex", 3, 30)
dog2 = Dog("Max", 5, 25)
dog3 = Dog("Buddy", 2, 20)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))





# Exercise 3 : Dogs Domesticated

import random
from dog import Dog  

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # Join all dog names together
        all_names = ", ".join([self.name] + list(args))
        print(f"{all_names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")


# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()





# Exercise 4 : Family and Person

class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        # Create a new Person and add to family
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, age: {member.age}")


# Test
my_family = Family("Williams")
my_family.born("Koe", 25)
my_family.born("Alice", 15)
my_family.born("Bob", 10)

my_family.check_majority("Koe")
my_family.check_majority("Alice")
my_family.family_presentation()