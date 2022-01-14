class Move:

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def is_valid(self):
        return 1 <= self.__value <= 9

    def get_row(self):
        if self.__value in (1, 2, 3):
            return 0
        elif self.__value in (4, 5, 6):
            return 1
        else:
            return 2

    def get_column(self):
        if self.__value in (1, 4, 7):
            return 0
        elif self.__value in (2, 5, 8):
            return 1
        else:
            return 2



move = Move(1)
print(move.value)
print(move.is_valid())
print(move.get_row())
print(move.get_column())