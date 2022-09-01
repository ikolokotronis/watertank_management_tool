from enums.States import States


class Tank:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.water_volume = 0
        self.options = {
            "1": self.pour_water,
            "2": self.pour_out_water,
            "3": self.transfer_water,
        }

    def pour_water(self, volume):
        if self.capacity - volume < 0:
            print("Tank does not have enough capacity!")
            return
        self.water_volume += volume
        return States.SUCCESS

    def pour_out_water(self, volume):
        if self.water_volume - volume < 0:
            print("Tank does not have this much water to pour out!")
            return States.FAILURE
        self.water_volume -= volume
        return States.SUCCESS

    def transfer_water(self, from_tank, volume):
        if self.water_volume + volume > self.capacity:
            print("Target tank does not have this much capacity!")
            return States.FAILURE
        if from_tank.water_volume - volume < 0:
            print("Sender does not have this much water!")
            return States.FAILURE
        self.water_volume += volume
        from_tank.water_volume -= volume
        return States.SUCCESS
