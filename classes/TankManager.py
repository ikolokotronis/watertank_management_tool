from classes.Messenger import Messenger
from constants.tank_options import TANK_OPTIONS
from exceptions.InvalidChoice import InvalidChoice
from factories.TankFactory import TankFactory


class TankManager:
    def __init__(self, tank_holder):
        self.tank_holder = tank_holder

    def create_new_tank(self):
        name = input('Tank name: ')
        capacity = int(input('Tank capacity: '))
        tank = TankFactory.produce(name, capacity)
        self.tank_holder.add_to_storage(tank)

    def view_all_tanks(self):
        if not self.tank_holder.storage:
            print('No tanks stored!')
            print('\n')
            return
        for i, tank in enumerate(self.tank_holder.storage):
            print(f'{tank.name}')
            print(f'Capacity: {tank.capacity}')
            print(f'Water volume: {tank.water_volume}')
            print('\n')

    def manage_tanks(self):
        if not self.tank_holder.storage:
            print('No tanks stored!')
            print('\n')
            return
        for i, tank in enumerate(self.tank_holder.storage):
            print('\n')
            print(f'{i+1}. {tank.name}')
            print(f'Capacity: {tank.capacity}')
            print(f'Water volume: {tank.water_volume}')
            print('\n')
        tank_choice = int(input('Tank to manage: '))
        tank = self.tank_holder.storage[tank_choice-1]
        print(f'You chose: {tank.name}')
        print('\n')
        for i, option in enumerate(TANK_OPTIONS):
            print(i+1, option)
        print('\n')
        operation_choice = input('Choose operation: ')
        volume_amount = int(input('Volume amount: '))
        try:
            operation = tank.options.get(operation_choice, Messenger.no_such_option)(volume_amount)
        except InvalidChoice:
            print("No such option!")
        print('Operation finished successfully') if operation else print('Operation failed')
        print('\n')