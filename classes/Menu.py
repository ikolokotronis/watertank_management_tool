from properties.OptionsProperty import OptionsPropety


class Menu:
    def __init__(self):
        self.options = OptionsPropety.MENU_OPTIONS.copy()

    def print_menu(self):
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")

    @staticmethod
    def get_choice():
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")
        return choice
