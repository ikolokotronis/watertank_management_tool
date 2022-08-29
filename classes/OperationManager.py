from classes.Messenger import Messenger
from constants.options import OPERATION_OPTIONS
from exceptions.InvalidChoice import InvalidChoice


class OperationManager:
    def __init__(self, tank_holder):
        self.options = {
            '1': self.find_tank_with_most_water_volume,
            '2': self.find_most_filled_tank,
            '3': self.find_empty_tanks
        }
        self.tank_holder = tank_holder

    def handle_operations(self):
        if not self.tank_holder.storage:
            print('No tanks stored!')
            print('\n')
            return
        for i, option in enumerate(OPERATION_OPTIONS):
            print(f"{i+1}. {option}")
        options = {
            '1': self.find_tank_with_most_water_volume,
            '2': self.find_most_filled_tank,
            '3': self.find_empty_tanks
        }
        choice = input('Your choice: ')
        try:
            options.get(choice, Messenger.no_such_option)()
        except InvalidChoice:
            print("No such option!")

    def find_tank_with_most_water_volume(self):
        if not self.tank_holder.storage:
            print('No tanks stored!')
            print('\n')
            return

        tank = max(self.tank_holder.storage)
        print(f'Name: {tank.name}')
        print(f'Capacity: {tank.capacity}')
        print(f'Water volume: {tank.water_volume}')
        print('\n')

    def find_most_filled_tank(self):
        pass

    def find_empty_tanks(self):
        if not self.tank_holder.storage:
            print('No tanks stored!')
            print('\n')
            return
        for i, tank in enumerate(self.tank_holder.storage):
            if tank.water_volume == 0:
                print(f'{tank.name}')
                print(f'Capacity: {tank.capacity}')
                print(f'Water volume: {tank.water_volume}')
                print('\n')