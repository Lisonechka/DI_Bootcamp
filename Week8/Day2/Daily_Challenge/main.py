from typing import List

class Farm:

    def __init__(self, name_of_farm: str):
        self.name = name_of_farm
        self.animals = {}

    def add_animal(self, animal: str, amount: int = 1) -> None:
        self.animals[animal] = self.animals.get(animal, 0) + amount

    def get_info(self) -> None:
        print(f"{self.name}'s farm\n")
        for animal_name, animal_count in self.animals.items():
            print(f"{animal_name}: {animal_count}")
        print("\tE-I-E-I-0!")

    def get_animal_types(self) -> List:
        return sorted(self.animals.keys())


farm = Farm('McDonald')
farm.add_animal('cow',5)
farm.add_animal('sheep')
farm.add_animal('sheep')
farm.add_animal('goat', 12)

farm.get_info()
print(farm.get_animal_types())