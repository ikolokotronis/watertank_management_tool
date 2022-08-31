import os


class States:
    SUCCESS = 1
    FAILURE = 0


class EventSourcerProperty:
    FILE_PATH = f'{os.getcwd()}/content/logs.txt'
