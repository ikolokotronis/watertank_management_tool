import datetime

from classes.Enum import States, EventSourcerProperty


class EventSourcer:
    def __init__(self):
        self.history = {}

    @staticmethod
    def create_event(name, tank, operation, status):
        event = {
            'name': name,
            'tank': tank,
            'operation': operation,
            'status': status,
            'date': datetime.datetime.now()
        }
        return event

    def add_to_history(self, event):
        self.history[event['name']] = event
        print('History:', self.history)

    def event_sourcing(self, f):
        def wrapper(operation_properties):
            state = f(operation_properties)
            if state == States.SUCCESS or state == States.FAILURE:
                raise ValueError("Invalid use of event sourcer!")
            event = EventSourcer.create_event(operation_properties['operation_name'], operation_properties['tank'],
                                              operation_properties['status'], operation_properties['operation_type'])
            self.history[event['operation_name']] = event
            print(event)
            # with open(EventSourcerProperty.FILE_PATH, 'w') as file:
            #     file.write(state)
        return wrapper
