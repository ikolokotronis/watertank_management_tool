from factories.menu_options import MENU_OPTIONS


class Menu:
    def __init__(self):
        self.options = MENU_OPTIONS.copy()

    def print_menu(self):
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    @staticmethod
    def get_choice():
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")
        return choice
