import datetime


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
        print('History: ', self.history)