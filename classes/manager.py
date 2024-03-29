from classes.event_sourcer import EventSourcer
from classes.menu import Menu
from classes.messenger import Messenger
from classes.tank_analyzer import TankAnalyzer
from classes.tank_manager import TankManager
from classes.tank_holder import TankHolder
from exceptions.invalid_choice import InvalidChoice


class Manager:
    def __init__(self):
        self.is_running = True
        self.menu = Menu()
        self.tank_holder = TankHolder()
        self.event_sourcer = EventSourcer(tank_holder=self.tank_holder)
        self.tank_analyzer = TankAnalyzer(
            tank_holder=self.tank_holder, event_sourcer=self.event_sourcer
        )
        self.tank_manager = TankManager(
            tank_holder=self.tank_holder, event_sourcer=self.event_sourcer
        )
        self.menu_options = {
            "1": self.tank_manager.create_new_tank,
            "2": self.tank_manager.execute_operation,
            "3": self.tank_holder.display_all_tanks,
            "4": self.tank_analyzer.execute_analysis,
            "5": self.event_sourcer.execute_state_check,
            "6": self.exit,
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
