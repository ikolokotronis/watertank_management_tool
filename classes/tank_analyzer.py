from enums.states import States
from classes.messenger import Messenger
from properties.options_property import OptionsPropety
from exceptions.invalid_choice import InvalidChoice
from utils.helpers import Helpers


class TankAnalyzer:
    def __init__(self, tank_holder, event_sourcer):
        self.options = {
            "1": self.find_tank_with_most_water_volume,
            "2": self.find_most_filled_tank,
            "3": self.find_empty_tanks,
            "4": self.find_tank_with_most_fails,
            "5": self.find_most_used_type,
        }
        self.tank_holder = tank_holder
        self.event_sourcer = event_sourcer

    def execute_analysis(self):
        if self.tank_holder.validate_storage() == States.FAILURE:
            return States.FAILURE
        for i, option in enumerate(OptionsPropety.OPERATION_OPTIONS):
            print(f"{i+1}. {option}")
        choice = input("\nYour choice: ")
        print("\n")
        try:
            self.options.get(choice, Messenger.no_such_option)()
        except InvalidChoice:
            print("No such option!")

    def find_tank_with_most_water_volume(self):
        if self.tank_holder.validate_storage() == States.FAILURE:
            return States.FAILURE
        water_volumes = [tank.water_volume for tank in self.tank_holder.storage]
        max_water_volume = max([tank.water_volume for tank in self.tank_holder.storage])
        tank_index = water_volumes.index(max_water_volume)
        tank = self.tank_holder.storage[tank_index]
        print(f"Name: {tank.name}")
        print(f"Capacity: {tank.capacity}")
        print(f"Water volume: {tank.water_volume}")
        print("\n")

    def find_most_filled_tank(self):
        if self.tank_holder.validate_storage() == States.FAILURE:
            return States.FAILURE
        calculations = []
        for tank in self.tank_holder.storage:
            calculation = tank.capacity - tank.water_volume
            calculations.append(calculation)
        tank_index = calculations.index(min(calculations))
        tank = self.tank_holder.storage[tank_index]
        print(f"Name: {tank.name}")
        print(f"Capacity: {tank.capacity}")
        print(f"Water volume: {tank.water_volume}")
        print("\n")

    def find_empty_tanks(self):
        empty_tanks = False
        for i, tank in enumerate(self.tank_holder.storage):
            if tank.water_volume == 0:
                empty_tanks = True
                print(f"{tank.name}")
                print(f"Capacity: {tank.capacity}")
                print(f"Water volume: {tank.water_volume}")
                print("\n")
        if not empty_tanks:
            print("There are no empty tanks!\n")
            return States.FAILURE

    def find_tank_with_most_fails(self):  # TODO ***
        failed_tank_statuses = {}
        for key, value in self.event_sourcer.history.items():
            for props_key, props_value in value.items():
                if props_key == "status" and props_value == 0:
                    failed_tank_statuses[key] = value
        if not failed_tank_statuses:
            print("No tanks have failed yet!\n")
            return States.FAILURE
        failed_tank_names = []
        for status_key, status_value in failed_tank_statuses.items():
            failed_tank_names.append(status_value["tank_name"])
        print(f"\nTank with most fails: {Helpers.most_common(failed_tank_names)}\n")
        return Helpers.most_common(failed_tank_names)

    def find_most_used_type(self):
        types = []
        for key, value in self.event_sourcer.history.items():
            for props_key, props_value in value.items():
                if props_key == "operation_type":
                    types.append(props_value)
        most_common_type = ""  # TODO as else
        try:
            most_common_type = Helpers.most_common(types)
        except ValueError:
            print("No operations have been done yet!\n")
            return States.FAILURE
        print(f"Most common type: {most_common_type}\n")
        return Helpers.most_common(types)
