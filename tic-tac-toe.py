from environment import *

def player_move(board, text):
    """ Get a player's move"""
    print('\n-------')
    print(text)
    move = None
    while move not in board.legal_moves():
        move = int(input('Select square to play at: '))-1
    return move

def play():
    """ Play Tic-Tac-Toe"""
    board = Board()
    board.output()
    player1 = input("What is X called? ")
    player2 = input("What is O called? ")
    print('{} is X and {} is O'.format(player1,player2))
    player = None
    while player not in ['X','O']:
         player = input('Who goes first?(X or O) ').capitalize()

    while not board.leaf():
        if player == 'X':
            move = player_move(board, '{}\'s turn'.format(player1))
            board.move(move, player)
        else:
            move = player_move(board, '{}\'s turn'.format(player2))
            board.move(move, player)
        board.output()
        player = get_opponent(player)

    if board.X_won():
        print("{} won!".format(player1))
    elif board.O_won():
        print("{} won!".format(player2))
    else:
        print("It's a tie!")

if __name__ == '__main__':
    play()
        
