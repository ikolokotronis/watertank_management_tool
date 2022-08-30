from classes.Enum import StateStatus
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

    def manage_tanks(self):
        if self.tank_holder.check_if_storage_is_empty() == StateStatus.FAILURE:
            return
        self.tank_holder.display_all_tanks()
        tank = self.get_tank_choice()
        for i, option in enumerate(TANK_OPTIONS):  # one method
            print(i+1, option)
        print('\n')
        operation_choice = input('Choose operation: ')
        event = {}
        if operation_choice == '1':
            volume_amount = int(input('Volume amount: '))
            operation_name = input('Name your operation: ')
            tank.pour_water(volume_amount)
            event = EventSourcer.create_event(operation_name, tank, StateStatus.SUCCESS, 'Pour water')
            self.event_sourcer.add_to_history(event)
        elif operation_choice == '2':
            volume_amount = int(input('Volume amount: '))
            operation_name = input('Name your operation: ')
            tank.pour_out_water(volume_amount)
            event = EventSourcer.create_event(operation_name, tank, StateStatus.SUCCESS, 'Pour out water')
            self.event_sourcer.add_to_history(event)
        elif operation_choice == '3':
            pass
        else:
            print('No such option!')
            return
        event_state = event['status']
        return event_state
