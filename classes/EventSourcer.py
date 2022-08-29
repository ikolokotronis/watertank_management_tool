class EventSourcer:
    def __init__(self):
        self.history = {}

    def add_to_history(self, operation):
        self.history[operation.name] = operation
