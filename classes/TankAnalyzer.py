from classes.Enum import States
from classes.Messenger import Messenger
from constants.options import OPERATION_OPTIONS
from exceptions.InvalidChoice import InvalidChoice
from utils.most_common import most_common


class TankAnalyzer:
    def __init__(self, tank_holder, event_sourcer):
        self.options = {
            '1': self.find_tank_with_most_water_volume,
            '2': self.find_most_filled_tank,
            '3': self.find_empty_tanks,
            '4': self.find_tank_with_most_fails,
            '5': self.find_most_used_type
        }
        self.tank_holder = tank_holder
        self.event_sourcer = event_sourcer

    def handle_operations(self):
        for i, option in enumerate(OPERATION_OPTIONS):
            print(f"{i+1}. {option}")
        choice = input('Your choice: ')
        try:
            self.options.get(choice, Messenger.no_such_option)()
        except InvalidChoice:
            print("No such option!")

    def find_tank_with_most_water_volume(self):
        tank = max(self.tank_holder.storage)
        print(f'Name: {tank.name}')
        print(f'Capacity: {tank.capacity}')
        print(f'Water volume: {tank.water_volume}')
        print('\n')

    def find_most_filled_tank(self):
        calculations = []
        for tank in self.tank_holder.storage:
            calculation = tank.capacity - tank.water_volume
            calculations.append(calculation)
        tank_index = calculations.index(min(calculations))
        tank = self.tank_holder.storage[tank_index]
        print(f'Name: {tank.name}')
        print(f'Capacity: {tank.capacity}')
        print(f'Water volume: {tank.water_volume}')
        print('\n')

    def find_empty_tanks(self):
        for i, tank in enumerate(self.tank_holder.storage):
            if tank.water_volume == 0:
                print(f'{tank.name}')
                print(f'Capacity: {tank.capacity}')
                print(f'Water volume: {tank.water_volume}')
                print('\n')

    def find_tank_with_most_fails(self):
        failed_tank_statuses = {}
        for key, value in self.event_sourcer.history.items():
            for props_key, props_value in value.items():
                if props_key == 'status' and props_value == 0:
                    failed_tank_statuses[key] = value
        if not failed_tank_statuses:
            return States.FAILURE
        failed_tank_names = []
        for status_key, status_value in failed_tank_statuses.items():
            failed_tank_names.append(status_value['tank_name'])
        print(f"\nTank with most fails: {most_common(failed_tank_names)}\n")
        return most_common(failed_tank_names)

    def find_most_used_type(self):
        types = []
        for key, value in self.event_sourcer.history.items():
            for props_key, props_value in value.items():
                if props_key == 'operation_type':
                    types.append(props_value)
        print(f'Most common type: {most_common(types)}')
        return most_common(types)
