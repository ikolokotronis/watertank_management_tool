from enums.states import States
from classes.event_sourcer import EventSourcer
from properties.options_property import OptionsPropety
from factories.tank_factory import TankFactory


class TankManager:
    def __init__(self, tank_holder, event_sourcer):
        self.tank_holder = tank_holder
        self.event_sourcer = event_sourcer

    def create_new_tank(self):
        name = input("Tank name: ")
        try:
            capacity = int(input("Tank capacity: "))
        except ValueError:
            print("Only numbers allowed!")
            return States.FAILURE
        tank = TankFactory.produce(name, capacity)
        self.tank_holder.add_to_storage(tank)
        print(f"Tank {name} created successfully!\n")

    def get_tank_from_choice(self):
        tank_choice = int(input("Tank to manage: "))
        tank = ""
        try:
            tank = self.tank_holder.storage[tank_choice - 1]
        except IndexError:
            print("No such tank!")
            return States.FAILURE
        print(f"You chose: {tank.name}")
        print("\n")
        return tank

    def execute_operation(self):
        if self.tank_holder.validate_storage() == States.FAILURE:
            return States.FAILURE
        self.tank_holder.display_all_tanks()
        try:
            tank = self.get_tank_from_choice()
        except IndexError:
            print("No such tank!")
            return States.FAILURE
        else:
            self.manage_tank_operations(tank)
        return States.SUCCESS

    def handle_pour_water(self, tank):
        try:
            volume_amount = int(input("Volume amount: "))
        except ValueError:
            print("Only numbers allowed!")
            return States.FAILURE
        operation_name = input("Name your operation: ")
        operation = tank.pour_water(volume_amount)
        operation_type = "Pour water"
        if operation:
            status = States.SUCCESS
        else:
            status = States.FAILURE
        return operation_name, operation_type, volume_amount, status

    def handle_pour_out_water(self, tank):
        try:
            volume_amount = int(input("Volume amount: "))
        except ValueError:
            print("Only numbers allowed!")
            return States.FAILURE
        operation_name = input("Name your operation: ")
        operation = tank.pour_out_water(volume_amount)
        operation_type = "Pour out water"
        if operation:
            status = States.SUCCESS
        else:
            status = States.FAILURE
        return operation_name, operation_type, volume_amount, status

    def handle_transfer_water(self, tank):
        self.tank_holder.display_all_tanks()
        from_tank_choice = input("From tank: ")
        try:
            from_tank = self.tank_holder.storage[int(from_tank_choice) - 1]
        except ValueError and IndexError:
            print("No such tank!")
            return States.FAILURE
        try:
            volume_amount = int(input("Volume amount: "))
        except ValueError:
            print("Only numbers allowed!")
            return States.FAILURE
        operation_name = input("Name your operation: ")
        operation = tank.transfer_water(from_tank, volume_amount)
        operation_type = "Transfer water"
        if operation:
            status = States.SUCCESS
        else:
            status = States.FAILURE
        return operation_name, operation_type, volume_amount, status

    @EventSourcer.enable_sourcing
    def manage_tank_operations(self, tank):
        for i, option in enumerate(OptionsPropety.TANK_OPTIONS):  # one method
            print(i + 1, option)
        print("\n")
        operation_choice = input("Choose operation: ")
        operation_name = ""
        operation_type = ""
        volume_amount = ""
        status = ""
        if operation_choice == "1":
            (
                operation_name,
                operation_type,
                volume_amount,
                status,
            ) = self.handle_pour_water(tank)
            print('Water poured in!')
            print(f'Tank {tank.name} now has {tank.water_volume} ')
        elif operation_choice == "2":
            (
                operation_name,
                operation_type,
                volume_amount,
                status,
            ) = self.handle_pour_out_water(tank)
            print('Water poured out!')
            print(f'Tank {tank.name} now has {tank.water_volume} ')
        elif operation_choice == "3":
            (
                operation_name,
                operation_type,
                volume_amount,
                status,
            ) = self.handle_transfer_water(tank)
            print(f'Water transferred!')
            print(f'Tank {tank.name} now has {tank.water_volume} ')
        else:
            print("No such option!")
            status = States.FAILURE
            return status
        operation_properties = {
            "operation_choice": operation_choice,
            "operation_type": operation_type,
            "operation_name": operation_name,
            "water_volume": volume_amount,
            "status": status,
            "tank": tank,
        }
        if status == States.FAILURE:
            print(f"\nOperation {operation_type} on tank {tank.name} failed")
            return States.FAILURE
        return operation_properties
