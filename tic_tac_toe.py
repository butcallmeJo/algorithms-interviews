#!usr/bin/env python

"""
Write a Tic Tac Toe game w/ inputs ...
"""

import sys

def init_board():
    board = [[" " for x in range(3)] for y in range(3)]
    for line in board:
        print line
    return board

def print_board(board):
    for line in board:
        print line

def get_input(board, letter):
    player_input = raw_input("Player %i please put an input (format: row column): ")
    if player_input == "exit":
        sys.exit()
    if not player_input:
        print "error, please input coordinates correctly."
        get_input(board, letter)
    player_input.split()
    row = int(player_input[0])
    column = int(player_input[2])
    
    if board[row][column] == ' ':
        board[row][column] = letter
    else:
        print "error, space already taken. try again"
        get_input(board, letter)
    return board

def check_win_conditions(bo, le):
    return (
        (bo[0][0] == le and bo[0][1] == le and bo[0][2] == le) or
        (bo[1][0] == le and bo[1][1] == le and bo[1][2] == le) or
        (bo[2][0] == le and bo[2][1] == le and bo[2][2] == le) or
        (bo[0][0] == le and bo[1][0] == le and bo[2][0] == le) or
        (bo[0][1] == le and bo[1][1] == le and bo[2][1] == le) or
        (bo[0][2] == le and bo[1][2] == le and bo[2][2] == le) or
        (bo[0][0] == le and bo[1][1] == le and bo[2][2] == le) or
        (bo[2][0] == le and bo[1][1] == le and bo[0][2] == le)
    )

def what_next():
    if raw_input("exit or play again? ('exit' or 'play'): ") == "play":
        main()
    else:
        sys.exit()

def main():
    new_board = init_board()
    for i in range(9):
        if i % 2 == 0:
            letter = 'X'
        else:
            letter = 'O'
        new_board = get_input(new_board, letter)
        print_board(new_board)
        if check_win_conditions(new_board, letter):
            print "%s wins!!!!" % (letter)
            what_next()
    print "No one won...good match!"
    what_next()

if __name__ == "__main__":
    main()