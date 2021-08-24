class Farm:

    def __init__(self, name_of_farm):
        self.name = name_of_farm
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal not in self.animals:
            print(f'{animal}: {amount}')
        else:
            print(f'{animal}: {amount + 1}')

    def get_info(self):
        print(f"{self.name}'s farm")


macdonald = Farm("McDonald")
print(macdonald.get_info())
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)


# McDonald's farm
#
# cow : 5
# sheep : 2
# goat : 12

# E-I-E-I-0!
