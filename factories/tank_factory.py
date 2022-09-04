from classes.tank import Tank


class TankFactory:
    @staticmethod
    def produce(name, capacity):
        return Tank(name, capacity)
