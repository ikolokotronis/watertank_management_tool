from classes.Menu import Menu
from classes.TankStorage import TankHolder
from factories.TankFactory import TankFactory
from factories.tank_options import TANK_OPTIONS


class Manager:
    def __init__(self):
        self.is_running = True
        self.menu = Menu()
        self.tank_holder = TankHolder()
        self.menu_options = {
            '1': self.create_new_tank,
            '2': self.manage_tanks,
            '3': self.view_all_tanks,
            '4': self.exit
        }

    def exit(self):
        self.is_running = False

    def run(self):
        while self.is_running is True:
            self.menu.print_menu()
            choice = self.menu.get_choice()
            self.__execute(choice)

    def show_error(self):
        print('No such option!')

    def __execute(self, choice):
        self.menu_options.get(choice, self.show_error)()

    def create_new_tank(self):
        name = input('Tank name: ')
        capacity = int(input('Tank capacity: '))
        tank = TankFactory.produce(name, capacity)
        self.tank_holder.add_to_storage(tank)

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
        operation = tank.options.get(operation_choice, None)(volume_amount)
        print('Operation finished successfully') if operation else print('Operation failed')
        print('\n')

    def view_all_tanks(self):
        if not self.tank_holder.storage:
            print('No tanks stored!')
            print('\n')
        for i, tank in enumerate(self.tank_holder.storage):
            print(f'{tank.name}')
            print(f'Capacity: {tank.capacity}')
            print(f'Water volume: {tank.water_volume}')
            print('\n')
