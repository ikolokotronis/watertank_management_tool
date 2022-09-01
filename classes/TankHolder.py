from enums.States import States


class TankHolder:
    def __init__(self):
        self.storage = []

    def add_to_storage(self, tank):
        self.storage.append(tank)
        print("\n")
        print("Tank added to storage")
        print("\n")

    def validate_storage(self):
        if len(self.storage) == 0:
            print("No tanks stored!\n")
            return States.FAILURE
        return States.SUCCESS

    def display_all_tanks(self):
        if self.validate_storage() == States.FAILURE:
            return States.FAILURE
        for i, tank in enumerate(self.storage):
            print("\n")
            print(f"{i+1} {tank.name}")
            print(f"Capacity: {tank.capacity}")
            print(f"Water volume: {tank.water_volume}")
            print("\n")
