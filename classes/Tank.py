class Tank:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.water_volume = 0
        self.options = {
            '1': self.pour_water,
            '2': self.pour_out_water,
            '3': self.transfer_water
        }

    def pour_water(self, volume):
        if self.capacity - volume < 0:
            print('Tank does not have enough capacity!')
            return
        self.water_volume += volume
        return 'success'

    def pour_out_water(self, volume):
        if self.water_volume - volume < 0:
            print('Tank does not have this much water to pour out!')
            return
        self.water_volume -= volume
        return 'success'

    def transfer_water(self, from_tank, volume):  # if or match case
        if self.water_volume + volume > self.capacity:
            print('Tank does not have this much capacity!')
            return
        self.water_volume += volume
        from_tank.capacity -= volume
        return 'success'
