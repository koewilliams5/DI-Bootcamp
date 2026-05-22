

# Daily Challenge : Old MacDonald's Farm

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        # If animal exists, add to its count
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            # If animal doesn't exist, create it
            self.animals[animal_type] = count

    def get_info(self):
        # Build the output string
        result = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"

        result += "\n    E-I-E-I-0!"
        return result

    # Bonus : get sorted list of animal types
    def get_animal_types(self):
        return sorted(self.animals.keys())

    # Bonus : get short info
    def get_short_info(self):
        animal_list = self.get_animal_types()

        # Add "s" if count > 1
        animals_str = []
        for animal in animal_list:
            if self.animals[animal] > 1:
                animals_str.append(animal + "s")
            else:
                animals_str.append(animal)

        return f"{self.name}'s farm has {', '.join(animals_str)}."


# Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_short_info())






