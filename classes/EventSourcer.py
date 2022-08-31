import datetime

from classes.Enum import States


class EventSourcer:
    def __init__(self):
        self.history = {}

    @staticmethod
    def create_event(operation_name, tank, status, operation_type, water_volume):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        event = {
            'operation_name': operation_name,
            'tank': tank,
            'operation_type': operation_type,
            'water_volume': water_volume,
            'status': status,
            'date_time': date_time
        }
        return event

    def add_to_history(self, event):
        self.history[event['operation_name']] = event
        print('History:', self.history)

    @staticmethod
    def event_sourcing(f):
        def wrapper(tank_manager, tank):
            state = f(tank_manager, tank)
            if state == States.SUCCESS or state == States.FAILURE:
                raise ValueError("Invalid use of event sourcer!")
            event = EventSourcer.create_event(state['operation_name'], state['tank'],
                                              state['status'], state['operation_type'],
                                              state['water_volume'])
            tank_manager.event_sourcer.add_to_history(event)
            # with open(EventSourcerProperty.FILE_PATH, 'w') as file:
            #     file.write(f'Operation name: {state["operation_name"]}'
            #                f'Operation status: {state["status"]}')
        return wrapper
