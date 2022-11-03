import datetime

from enums.states import States
from properties.event_sourcer_property import EventSourcerProperty


class EventSourcer:
    def __init__(self, tank_holder):
        self.tank_holder = tank_holder
        self.history = {}

    def get_tank_choice(self):
        tank_choice = int(input("Tank choice: "))
        try:
            tank = self.tank_holder.storage[tank_choice - 1]
        except IndexError:
            print('No such tank!')
        else:
            print(f"You chose: {tank.name}")
            print("\n")
            return tank

    def execute_state_check(self):
        if self.tank_holder.validate_storage() == States.FAILURE:
            return States.FAILURE
        self.tank_holder.display_all_tanks()
        tank = self.get_tank_choice()
        self.check_state(tank)

    def calculate_state_volume(self, tank):
        state_volume = 0
        for key, value in self.history.items():
            if value["tank_name"] == tank.name: # TODO -> extract into seperated methods; replace imperative with declarative
                items = [i for i in value.items()]
                if "Pour water" in items[2]:  # remove string, make class
                    for props_key, props_value in items:
                        if props_key == "water_volume":
                            state_volume += props_value
                elif "Pour out water" in items[2]:
                    for props_key, props_value in items:
                        if props_key == "water_volume":
                            state_volume -= props_value
                elif "Transfer water" in items[2]:
                    for props_key, props_value in items:
                        if props_key == "water_volume":
                            state_volume += props_value
        return state_volume

    def check_state(self, tank):
        state_volume = self.calculate_state_volume(tank)
        if tank.water_volume == state_volume:
            print("OK\n")
            return States.SUCCESS
        print("NOT OK\n")
        return States.FAILURE

    @staticmethod
    def create_event(operation_name, tank, status, operation_type, water_volume):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        event = {
            "operation_name": operation_name,
            "tank_name": tank.name,
            "operation_type": operation_type,
            "water_volume": water_volume,
            "status": status,
            "date_time": date_time,
        }
        return event

    def add_to_history(self, event):
        self.history[event["operation_name"]] = event

    @classmethod
    def write_to_logs(cls, state):
        with open(EventSourcerProperty.FILE_PATH, "a") as file:
            file.write(
                f'Operation name: {state["operation_name"]}\n'
                f'Operation status: {state["status"]}\n'
                f'Operation type: {state["operation_type"]}\n'
                f'Tank: {state["tank"].name}\n'
                f'Water volume: {state["water_volume"]}\n'
            )
        return States.SUCCESS

    @staticmethod
    def enable_sourcing(f):
        def wrapper(tank_manager, tank):
            state = f(tank_manager, tank)
            if state == States.SUCCESS or state == States.FAILURE:
                return States.FAILURE
            event = EventSourcer.create_event(
                state["operation_name"],
                state["tank"],
                state["status"],
                state["operation_type"],
                state["water_volume"],
            )
            tank_manager.event_sourcer.add_to_history(event)
            tank_manager.event_sourcer.write_to_logs(state)

        return wrapper
