import numpy as np
import random

board = np.array([[0,0,0],
                  [0,0,0],
                  [0,0,0]])
moves = []

def print_board(board):

    print(board)


def check_win(board):
    for i in range(0,3):
        if board[i][0]==1 and board[i][1]==1 and board[i][2]==1 or board[0][i]==1 and board[1][i]==1 and board[2][i]==1:
            print("player won")
            return True
        elif board[i][0]==2 and board[i][1]==2 and board[i][2]==2 or board[0][i]==2 and board[1][i]==2 and board[2][i]==2:
            print("computer won")
            return True
        elif board[0][0]==1 and board[1][1]==1 and board[2][2]==1 or board[0][2]==1 and board[1][1]==1 and board[2][0]==1:
            print("player won")
            return True
        elif board[0][0]==2 and board[1][1]==2 and board[2][2]==2 or board[0][2]==2 and board[1][1]==2 and board[2][0]==2:
            print('computer won')
            return True


def player_move(board, moves):
    print("****player move****")
    print_board(board)
    move = int(input("enter number(1-9) : "))
    if move not in moves:
        if move == 1:
            board[0][0]=1
            moves.append(1)
        if move == 2:
            board[0][1]=1
            moves.append(2)
        if move == 3:
            board[0][2]=1
            moves.append(3)
        if move == 4:
            board[1][0]=1
            moves.append(4)
        if move == 5:
            board[1][1]=1
            moves.append(5)
        if move == 6:
            board[1][2]=1
            moves.append(6)
        if move == 7:
            board[2][0]=1
            moves.append(7)
        if move == 8:
            board[2][1]=1
            moves.append(8)
        if move == 9:
            board[2][2]=1
            moves.append(9)
        # elif move>9:
        #     print("enter a valid value")
        #     player_move(board, moves)

    print_board(board)

def comp_move(board, moves):
    move = random.randint(1,9)
    if move not in moves:
        print("****computer move****")
        if move == 1:
            board[0][0]=2
            moves.append(1)
        if move == 2:
            board[0][1]=2
            moves.append(2)
        if move == 3:
            board[0][2]=2
            moves.append(3)
        if move == 4:
            board[1][0]=2
            moves.append(4)
        if move == 5:
            board[1][1]=2
            moves.append(5)
        if move == 6:
            board[1][2]=2
            moves.append(6)
        if move == 7:
            board[2][0]=2
            moves.append(7)
        if move == 8:
            board[2][1]=2
            moves.append(8)
        if move == 9:
            board[2][2]=2
            moves.append(9)
        print_board(board)
    else:
        comp_move(board, moves)

def play_game():
    player_move(board, moves)
    check_win(board)
    comp_move(board, moves)
    check_win(board)
i = 0
while not check_win(board):
    if i>=9 and not check_win(board):
        print("game tied")
    else:
        play_game()
        i+=1

# i = 0
# while i<=9:
#     play_game()
#     i+=2
