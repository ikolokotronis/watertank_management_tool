from classes.Tank import Tank


class TankFactory:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def produce(self):
        return Tank(self.name, self.capacity)