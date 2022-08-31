from classes.Enum import States
from classes.EventSourcer import EventSourcer
from constants.options import TANK_OPTIONS
from factories.TankFactory import TankFactory


class TankManager:
    def __init__(self, tank_holder, event_sourcer):
        self.tank_holder = tank_holder
        self.event_sourcer = event_sourcer

    def create_new_tank(self):
        name = input('Tank name: ')
        capacity = int(input('Tank capacity: '))
        tank = TankFactory.produce(name, capacity)
        self.tank_holder.add_to_storage(tank)

    def get_tank_choice(self):
        tank_choice = int(input('Tank to manage: '))
        tank = self.tank_holder.storage[tank_choice - 1]
        print(f'You chose: {tank.name}')
        print('\n')
        return tank

    def execute(self):
        if self.tank_holder.check_if_storage_is_empty() == States.FAILURE:
            return
        self.tank_holder.display_all_tanks()
        tank = self.get_tank_choice()
        self.manage_tank_operations(tank)

    @EventSourcer.event_sourcing
    def manage_tank_operations(self, tank):
        for i, option in enumerate(TANK_OPTIONS):  # one method
            print(i+1, option)
        print('\n')
        operation_choice = input('Choose operation: ')
        operation_type = ''
        volume_amount = ''
        if operation_choice == '1':
            volume_amount = int(input('Volume amount: '))
            operation_name = input('Name your operation: ')
            tank.pour_water(volume_amount)
            operation_type = 'Pour water'
        elif operation_choice == '2':
            volume_amount = int(input('Volume amount: '))
            operation_name = input('Name your operation: ')
            tank.pour_out_water(volume_amount)
            operation_type = 'Pour out water'
        elif operation_choice == '3':
            self.tank_holder.display_all_tanks()
            from_tank_choice = input('From tank: ')
            from_tank = self.tank_holder.storage[int(from_tank_choice) - 1]
            volume_amount = int(input('Volume amount: '))
            operation_name = input('Name your operation: ')
            tank.transfer_water(from_tank, volume_amount)
            operation_type = 'Transfer water'
        else:
            print('No such option!')
            return
        operation_properties = {
            'operation_choice': operation_choice,
            'operation_type': operation_type,
            'operation_name': operation_name,
            'water_volume': volume_amount,
            'status': States.SUCCESS,
            'tank': tank
        }
        return operation_properties
