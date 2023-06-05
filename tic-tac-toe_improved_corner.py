import numpy as np
import random
boxes = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
def print_board(boxes):
    print('  |   |')
    print('{} | {} | {}'.format(boxes[1], boxes[2], boxes[3]))
    print('----------')
    print('{} | {} | {}'.format(boxes[4], boxes[5], boxes[6]))
    print('----------')
    print('{} | {} | {}'.format(boxes[7], boxes[8], boxes[9]))
    print('  |   |')

def player_move():
    player_pos = int(input('Players Turn: '))
    if boxes[player_pos] == 'X' or boxes[player_pos] == 'O':
        print('space already taken')
        player_move()
    else:
        if player_pos >= 1 and player_pos <= 9:
            boxes[player_pos] = 'X'

        else:
            print('value should be between 1 and 9')
            player_move()
def computer_move():
    rand_num = np.random.randint(1,9)
    if boxes[rand_num] == 'X' or boxes[rand_num] == 'O':
        computer_move()
    else:
        boxes[rand_num] = 'O'
    # print('computers turn')

def eval(boxes):

    empty_spaces = []
    for i in boxes:
        if boxes[i] == ' ':
            empty_spaces.append(i)


    if boxes[1]=='X' and boxes[2]=='X' and boxes[3] == 'X':
        return 1
    elif boxes[4]=='X' and boxes[5]=='X' and boxes[6] == 'X':
        return 1
    elif boxes[7]=='X' and boxes[8]=='X' and boxes[9] == 'X':
        return 1
    elif boxes[1]=='X' and boxes[4]=='X' and boxes[7] == 'X':
        return 1
    elif boxes[2]=='X' and boxes[5]=='X' and boxes[8] == 'X':
        return 1
    elif boxes[3]=='X' and boxes[6]=='X' and boxes[9] == 'X':
        return 1
    elif boxes[1]=='X' and boxes[5]=='X' and boxes[9] == 'X':
        return 1
    elif boxes[3]=='X' and boxes[5]=='X' and boxes[7] == 'X':
        return 1


    elif boxes[1]=='O' and boxes[2]=='O' and boxes[3] == 'O':
        return -1
    elif boxes[4]=='O' and boxes[5]=='O' and boxes[6] == 'O':
        return -1
    elif boxes[7]=='O' and boxes[8]=='O' and boxes[9] == 'O':
        return -1
    elif boxes[1]=='O' and boxes[4]=='O' and boxes[7] == 'O':
        return -1
    elif boxes[2]=='O' and boxes[5]=='O' and boxes[8] == 'O':
        return -1
    elif boxes[3]=='O' and boxes[6]=='O' and boxes[9] == 'O':
        return -1
    elif boxes[1]=='O' and boxes[5]=='O' and boxes[9] == 'O':
        return -1
    elif boxes[3]=='O' and boxes[5]=='O' and boxes[7] == 'O':
        return -1
    else:
        return 0

def smartmove(boxes):
    boxes_copy = boxes
    empty_spaces = []
    for i in boxes_copy:
        if boxes_copy[i] == ' ':
            empty_spaces.append(i)
    for move in ['O', "X"]:
        if move == 'O':
            for empty in empty_spaces:
                boxes_copy[empty] = 'O'
                if eval(boxes_copy) == -1:
                    boxes[empty] = move
                    return True
                else:
                    boxes_copy[empty] = ' '
        else:
            for empty in empty_spaces:
                boxes_copy[empty] = move
                if eval(boxes_copy) == 1:
                    boxes[empty] = 'O'
                    return True
                else:
                    boxes_copy[empty] = ' '
    return False

    print_board(boxes)

def take_corner(boxes):
    boxes_copy = boxes
    corners = [1,3,7,9]
    empty_corners = []
    for i in corners:
        if boxes_copy[i] == ' ':
            empty_corners.append(i)
    if len(empty_corners)>0:
        random_corner = random.choice(empty_corners)
        boxes[random_corner] = 'O'
        return True
    else:
        return False



def play_game():
    try:
        for no in range(10):
            print_board(boxes)
            player_move()
            print('-----------------------------')
            if eval(boxes) == 1:
                print('-------------------------------------')
                print('you won')
                print_board(boxes)
                break
            print('computers turn')
            if smartmove(boxes) == False:
                if take_corner(boxes) == False:
                    computer_move()

            if eval(boxes) == -1:
                print('----------------------')
                print('computer won')
                print_board(boxes)
                break

    except  RecursionError:
        print('game tied')
        print_board(boxes)

play_game()




'''still to do :-
1. take the corner if free'''
