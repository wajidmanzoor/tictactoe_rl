import numpy as np
board = -1*np.ones((3,3),dtype='int32')
weights = np.zeros((9,9))
board[0][0] = 1
board[2][2] =0

def print_(board):
    for i in range(3):
        temp=' '
        c=0
        for j in board[:,i]:
            if j != -1:
                temp+=str(j)
            else:
                temp+=' '
            if c!=2:
                temp+=' |'
            c+=1
        print(temp)
        if i!=2:
            print("________")

def choose(board,pos,sign):
    board[pos[0]][pos[1]]=sign
    return board

            