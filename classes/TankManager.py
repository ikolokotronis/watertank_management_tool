from classes.Messenger import Messenger
from constants.options import TANK_OPTIONS
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
        if not self.tank_holder.storage:  # one method (validation)
            print('No tanks stored!\n')
            return
        for i, tank in enumerate(self.tank_holder.storage):  # one method (display tanks)
            print('\n')
            print(f'{i+1}. {tank.name}')
            print(f'Capacity: {tank.capacity}')
            print(f'Water volume: {tank.water_volume}')
            print('\n')
        tank_choice = int(input('Tank to manage: '))  # one method
        tank = self.tank_holder.storage[tank_choice-1]
        print(f'You chose: {tank.name}')
        print('\n')
        for i, option in enumerate(TANK_OPTIONS):  # one method
            print(i+1, option)
        print('\n')
        operation_choice = input('Choose operation: ')
        volume_amount = int(input('Volume amount: '))
        try:
            operation_state = tank.options.get(operation_choice, Messenger.no_such_option)(volume_amount)
        except InvalidChoice:
            print("No such option!")
            print('Operation failed')
        else:
            print('Operation finished successfully')
            print('\n')

        return operation_state