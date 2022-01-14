from move import Move
from player import Player
from board import Board


class TicTacToeGgame:

    def start(self):
        print('*************************')
        print(' Welcome  to Tic-Tac-Toe')
        print('**************************')

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()

        while True:
            while True:

                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's a tie! Try agiain.")
                    break
                elif board.check_is_game_over(player, player_move):
                    print('Awsome. You won the game!')
                    break
                else:
                    computer_move = computer.get_move()
                    board.submit_move(computer, computer_move)
                    board.print_board()

                    if board.check_is_game_over(computer, computer_move):
                        print('Oops... The computer won. Try again.')
                        break
            
            play_again = input('Would you like to play again? Enter X for YES or O for NO: ').upper()

            if play_again == 'O':
                print('Bye! Come back soon')
                break
            elif play_again == 'X':
                self.start_new_round(board)
            else:
                print('Your input was not valid but I will asuume that you want to play again.')
                self.start_new_round(board)


    def start_new_round(self, board):
        print('****************')
        print('  New Round ')
        print('****************')
        board.reset_board()
        board.print_board()


game = TicTacToeGgame()
game.start()
