class TankHolder:
    def __init__(self):
        self.storage = []

    def add_to_storage(self, tank):
        self.storage.append(tank)
        print('\n')
        print('Tank added to storage')
        print('\n')