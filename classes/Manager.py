from classes.EventSourcer import EventSourcer
from classes.Menu import Menu
from classes.Messenger import Messenger
from classes.OperationManager import OperationManager
from classes.TankManager import TankManager
from classes.TankHolder import TankHolder
from exceptions.InvalidChoice import InvalidChoice


class Manager:
    def __init__(self):
        self.is_running = True
        self.menu = Menu()
        self.tank_holder = TankHolder()
        self.event_sourcer = EventSourcer()
        self.operation_manager = OperationManager(tank_holder=self.tank_holder, event_sourcer=self.event_sourcer)
        self.tank_manager = TankManager(tank_holder=self.tank_holder, event_sourcer=self.event_sourcer)
        self.menu_options = {
            '1': self.tank_manager.create_new_tank,
            '2': self.tank_manager.manage_tanks,
            '3': self.tank_holder.display_all_tanks,
            '4': self.operation_manager.handle_operations,
            '5': self.exit
        }

    def exit(self):
        self.is_running = False

    def run(self):
        while self.is_running is True:
            self.menu.print_menu()
            choice = self.menu.get_choice()
            self.__execute(choice)

    def __execute(self, choice):
        try:
            self.menu_options.get(choice, Messenger.no_such_option)()
        except InvalidChoice:
            print("No such option!")
