from exceptions.invalid_choice import InvalidChoice


class Messenger:
    @staticmethod
    def no_such_option():
        raise InvalidChoice("No such option!")
