class Helpers:
    @staticmethod
    def most_common(lst):
        return max(set(lst), key=lst.count)
