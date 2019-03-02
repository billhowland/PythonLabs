# 26ttt.py
# Version 1: Tic Tac Toe


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    def __init__(self):
        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]

    def __repr__(self):
        board = ''
        for row in self.board:
            board += '|'.join(row) + '\n'
        return board

    def move(self, player, x, y):
        # figure out x, y
        if self.board[y][x] not in ['a', 'b']:
            self.board[y][x] = player
            return True
        else:
            return False


# ---------------------------------------------------------------

def spot_number(board, player):
    while True:
        try:
            # a = int(input())
            move = board.move(player, 0, 0)
            if move:
                break
            else:
                print("\nSpace Occupied, try again")
                break
        except ValueError:
            print("\nInvalid, try again")


def main():
    board = Game()
    players = []
    # board.board[1][1] = 'x'
    players.append(input("What is player one's name? > "))
    players.append(input("What is player two's name? > "))
    print("Great! Let's play some Tic Tac Toe!")
    for player in players:
        print(f'{player}, please pick a spot')
        spot_number(board, player)  # aint gonna work
        print(board)


# ----------------------------------------------------------------


if __name__ == '__main__':

    run = 1
    while run:

        main()

        ask = input('Quit? Y/N > ').strip().lower()
        if ask == 'y':
            run = 0
