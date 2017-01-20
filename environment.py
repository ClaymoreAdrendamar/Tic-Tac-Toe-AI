# Board environment class
class Board(object):
    """ Game Environment Class"""
    
    def __init__(self, board=[]):
        """ Initialize the environment variables """
        # Generate a new board if the passed board is empty
        if len(board) == 0:
            self.board = [' ' for square in range(9)]
        # Set new board as old board
        else:
            self.board = board

        self.winning_streaks = (
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6])

    def output(self):
        """ Print the board"""
        print()
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print('-----')
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print('-----')
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
        print()

    def legal_moves(self):
        """ Get the empty spaces """
        return [index for index, square in enumerate(self.board) if square == ' ']

    def leaf(self):
        """ Is the board full or has someone won the game """
        if ' ' not in [square for square in self.board]:
            return True
        if self.winner() != None:
            return True
        return False

    def X_won(self):
        """ Did player X win """
        return self.winner() == 'X'

    def O_won(self):
        """ Did player O win """
        return self.winner() == 'O'

    def tied(self):
        """ Is the game a tie? """
        return self.leaf() == True and self.winner() is None

    def winner(self):
        """ Get the winner of the board """
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for streak in self.winning_streaks:
                win = True
                for pos in streak:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """ Get a list of all squares taken by a certain player """
        return [index for index, square in enumerate(self.board) if square == player]

    def move(self, position, player):
        """ Move player to position """
        self.board[position] = player

def get_opponent(player):
    """ Gives us the opponent of player """
    if player == 'O':
        return 'X'
    else:
        return 'O'
