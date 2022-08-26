from classes.Menu import Menu
from classes.TankHolder import TankHolder
from factories.TankFactory import TankFactory


class Manager:
    def __init__(self):
        self.is_running = True
        self.menu = Menu()
        self.tank_holder = TankHolder()
        self.menu_options = {
            '1': self.create_new_tank
        }

    def exit(self):
        self.is_running = False

    def run(self):
        while self.is_running is True:
            self.menu.print_menu()
            choice = self.menu.get_choice()

    def __execute(self, choice):
        try:
            self.menu_options.get(choice, print('No such option!'))()
        except InvalidChoice:
            print("No such option!")

    def create_new_tank(self, name, capacity):
        tank = TankFactory(name, capacity)
        self.tank_holder.add_to_storage(tank)