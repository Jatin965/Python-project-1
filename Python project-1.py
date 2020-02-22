def  dboard(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])

def win(board,mark):
    return ((board[7]==board[8]==board[9]==mark) or (board[4]==board[5]==board[6]==mark) or (board[1]==board[2]==board[3]==mark) or 
    (board[7]==board[4]==board[5]==mark) or (board[5]==board[8]==board[2]==mark) or (board[6]==board[3]==board[9]==mark) or  
    (board[7]==board[5]==board[3]==mark) or (board[1]==board[5]==board[9]==mark))  

import random

def play():
    f=random.randint(0,1)
    if f ==0:
        return 'Player 1 '
    else:
        return 'Player 2 '
    
def space(board,position):
    return board[position]==' '

def fbspace(board):
    if ' ' in board[1:]:
        return False
    else:    
        return True

def nextp(board):
    pos=0
    while pos not in range(1,10) or not space(board,pos):
        pos=int(input('Choose a Position(1-9) : '  ))
        if board[pos] != ' ':
            print('That space is occupied ! ')
            continue    
    return pos

def replay():
    f=input('Do you want to play again?(Y/N) ').lower()
    return f=='y'

    
def  pin():
    marker=' '
    while marker!='X' and marker!='O':
        marker=input('Player 1 , choose X or O: ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

print(' Welcome to Tic Tac Toe!!')
while True:
    board=[' ']*10  
    p1,p2=pin()
    turn=play()
    print(turn + ' will go first ')
    game=input('Ready to play ? (Y/N) ').upper()
    while game =='Y':
        if turn == 'Player 1 ':
            dboard(board)
            pos=nextp(board)
            board[pos]=p1
            if win(board,p1):
                dboard(board)
                print('Player 1 won the game : ')
                game='N'
            if fbspace(board):
                dboard(board)
                print('Game Draw ')
                game='N'
            else:
                turn='Player 2 '
        else:
            dboard(board)
            pos=nextp(board)
            board[pos]=p2
            if win(board,p2):
                dboard(board)
                print('Player 2 won the game : ')
                game='N'
            else:
                if fbspace(board):
                    dboard(board)
                    print('Game Draw ')
                    game='N'
                else:
                    turn='Player 1 '
    if not replay():
        break