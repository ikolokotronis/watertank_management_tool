from classes.Menu import Menu
from classes.TankHolder import TankHolder
from factories.TankFactory import TankFactory


class Manager:
    def __init__(self):
        self.is_running = True
        self.menu = Menu()
        self.tank_holder = TankHolder()
        self.menu_options = {
            '1': self.create_new_tank,
            '2': self.view_all_tanks
        }

    def exit(self):
        self.is_running = False

    def run(self):
        while self.is_running is True:
            self.menu.print_menu()
            choice = self.menu.get_choice()
            self.__execute(choice)

    def __execute(self, choice):
        self.menu_options.get(choice, None)()

    def create_new_tank(self):
        name = input('Tank name: ')
        capacity = int(input('Tank capacity: '))
        tank = TankFactory(name, capacity)
        self.tank_holder.add_to_storage(tank)

    def view_all_tanks(self):
        for tank in self.tank_holder.storage:
            print(tank.name, tank.capacity)