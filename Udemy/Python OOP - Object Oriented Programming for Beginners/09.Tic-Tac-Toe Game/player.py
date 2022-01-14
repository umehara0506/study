import random

from move import Move


class Player:

    PLAYER_MARKER = 'X'
    COMPUTER_MARKER = 'O'

    def __init__(self, is_human=True):
        self.__is_human = is_human

        if is_human:
            self.__marker = Player.PLAYER_MARKER
        else:
            self.__marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self.__is_human

    @property
    def marker(self):
        return self.__marker

    def get_move(self):
        if self.__is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        while True:
            user_input = int(input('Please enter you move (1-9): '))
            move = Move(user_input)
            if move.is_valid():
                break
            else:
                print('Please enter an integer between 1 and 9.')
        return move

    def get_computer_move(self):
        while True:
            random_choice = random.choice(list(range(1, 10)))
            move = Move(random_choice)
            print('Computer move (1-9): ', move.value)
            return move
        



    