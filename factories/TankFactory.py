from classes.Tank import Tank


class TankFactory:
    # def __init__(self, name, capacity):
    #     self.name = name
    #     self.capacity = capacity
    @staticmethod
    def produce(name, capacity):
        return Tank(name, capacity)