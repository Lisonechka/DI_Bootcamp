# Exercise 3 : Restaurant Menu Manager
class MenuManager:
    menu = [
        {'Name': 'Soup', 'Price': 10, 'Spice': 'B', 'Gluten': False},
        {'Name': 'Hamburger', 'Price': 15, 'Spice': 'A', 'Gluten': True},
        {'Name': 'Salad', 'Price': 18, 'Spice': 'A', 'Gluten': False},
        {'Name': 'French Fries', 'Price': 5, 'Spice': 'C', 'Gluten': False},
        {'Name': 'Beef bourguignon', 'Price': 25, 'Spice': 'B', 'Gluten': True},
    ]

    def __init__(self):
        pass

    def add_item(self, name, price, spice, gluten):
        self.menu.append({'Name': name, 'Price': price, 'Spice': spice, 'Gluten': gluten})

    def update_item(self, name, price, spice, gluten):
        for i in self.menu:
            if name == i.get('Name'):
                updated_i = {'Name': name, 'Price': price, 'Spice': spice, 'Gluten': gluten}
                i.update(updated_i)
                print(f"{name} has been updated: {i} ")
            else:
                pass
        print(f'The dish {name} is not in the menu')

    def remove_item(self, name):
        for i in self.menu:
            if name == i.get('Name'):
                self.menu.remove(i)
                print(f'{name} is removed from the menu')
            else:
                pass
        print(f'The dish {name} is not in the menu')


dish = MenuManager()
dish.add_item('Tea', 10, 'A', False)
print(dish.menu)
dish.update_item('Steak', 60, 'A', False)
dish.remove_item('Soup')
dish.remove_item('Coffee')
