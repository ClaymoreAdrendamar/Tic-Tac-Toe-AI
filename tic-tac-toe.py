from environment import *
from copy import deepcopy

def player_move(board, text):
    """ Get a player's move"""
    print('\n-------')
    print(text)
    move = None
    while move not in board.legal_moves():
        move = int(input('Select square to play at: '))-1
    return move

def computer_move(board, computer):
    """ Get the stupod computer's move """
    board = deepcopy(board) # Copy board as we will be changing it
    best_moves = [0,2,6,8,4,1,3,5,7]
    player = get_opponent(computer)

    # If computer can win: play there
    for move in board.legal_moves():
        board.move(move, computer)
        if board.winner() == computer:
            print('Computer will play at square: {}'.format(move+1))
            return move
        # Undo the move
        board.move(move, ' ')
        
    # If player can win: block the move
    for move in board.legal_moves():
        board.move(move, player)
        if board.winner() == player:
            print('Computer will play at square: {}'.format(move+1))
            return move
        # Undo the move
        board.move(move, ' ')

    # Else pick the best empty square
    for move in best_moves:
        if move in board.legal_moves():
            print('Computer will play at square: {}'.format(move+1))
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
         player = input('Who goes first(X or O)? ').capitalize()

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

def computer_play():
    """ Play Tic-Tac-Toe against a (stupid) computer"""
    board = Board()
    board.output()
    player1 = input("What are you called? ")
    player2 = "Computer"
    print('{} is X and {} is O'.format(player1,player2))
    player = None
    while player not in ['X','O']:
         player = input('Who goes first?(X or O) ').capitalize()

    while not board.leaf():
        if player == 'X':
            move = player_move(board, '{}\'s turn'.format(player1))
            board.move(move, player)
        else:
            move = computer_move(board, player)
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
    computer_play()
        
