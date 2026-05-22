# Exercise 1 : Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Fluffy", 3)
cat2 = Cat("Kiokiou", 1)
cat3 = Cat("Goulley", 7)

# Step 2: Find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1
    elif cat2.age > cat1.age and cat2.age > cat3.age:
        return cat2
    else:
        return cat3

# Step 3: Print the oldest cat's details
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")





# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2}cm high!")


# Step 2: Create dog objects
davids_dog = Dog("Pitbull", 120)
sarahs_dog = Dog("Malinois", 160)

# Step 3: Print details and call methods
print(f"Name: {davids_dog.name}, Height: {davids_dog.height}cm")
davids_dog.bark()
davids_dog.jump()

print(f"Name: {sarahs_dog.name}, Height: {sarahs_dog.height}cm")
sarahs_dog.bark()
sarahs_dog.jump()

# Step 4: Compare dog sizes
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger!")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger!")
else:
    print("Both dogs are the same size!")





# Exercise 3 : Who's the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # Print each line of the lyrics
        for line in self.lyrics:
            print(line)


# Create a song object
stairway = Song(["There's a lady who's sure", 
                 "all that glitters is gold", 
                 "and she's buying a stairway to heaven"])

stairway.sing_me_a_song()





# Exercise 4 : A Day at the Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        # Add only if animal doesn't exist yet
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} already exists!")

    def get_animals(self):
        # Display all animals
        print(f"Animals in {self.zoo_name}: {self.animals}")

    def sell_animal(self, animal_sold):
        # Remove animal if it exists
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold!")
        else:
            print(f"{animal_sold} not found!")

    def sort_animals(self):
        # Sort and group by first letter
        sorted_list = sorted(self.animals)
        groups = {}

        for animal in sorted_list:
            first_letter = animal[0]
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)

        return groups

    def get_groups(self):
        # Print the grouped animals
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Lion")
brooklyn_safari.add_animal("Zebra")
brooklyn_safari.add_animal("Cat")
brooklyn_safari.add_animal("Cougar")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()




    
























