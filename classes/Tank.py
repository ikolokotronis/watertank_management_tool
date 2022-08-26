class Tank:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.water_volume = 0
        self.options = {
            '1': self.pour_water,
            '2': self.pour_out_water
        }

    def pour_water(self, volume):
        if self.capacity - volume < 0:
            print('Tank does not have enough capacity!')
            return
        self.water_volume += volume

    def pour_out_water(self, volume):
        if self.capacity - volume < self.capacity:
            print('Tank does not have this much water to pour out!')
            return
        self.capacity = self.capacity - volume

    def transfer_water(self, from_tank, volume):
        if self.capacity + volume > self.capacity:
            print('Tank does not have this much capacity!')
            return
        self.capacity = self.capacity + volume
        from_tank.capacity = from_tank.capacity - volume

