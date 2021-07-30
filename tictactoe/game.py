import numpy as np
board = -1*np.ones((3,3),dtype='int32')
weights = np.zeros((9,9))
"""board[0][0] = 1
board[2][2] =0"""
choice_board = np.array([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)])
index = np.array([0,1,2,3,4,5,6,7,8])

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
    print('\n \n')

def choose(board,pos,sign):
    board[pos[0]][pos[1]]=sign
    return board

def play(board,weights,choice_board,index):
   
    while True :
        toss_input = int(input('choose Head(0) or Tail(1)'))
        toss = np.random.choice([0,1])
        if toss_input == toss:
            print('congrats you won the toss ! \n \n your sign is 0')
            while True:
                if not np.any((board==-1)):
                    print('zook')
                    break
               
                while True:
                    choice_pos = int(input('Choose a position on board (0-8)'))
                    if choice_pos in index[(board==-1).flatten()]:
                        choice_pos = choice_board[choice_pos]
                        break
                    print('Choose again retard ')
                board = choose(board,choice_pos,0)
                print_(board)
                try:
                    random_pos = choice_board[np.random.choice(index[(board==-1).flatten()])]
                except:
                    random_pos=None
                if random_pos is None:
                    break
                board = choose(board,random_pos,1)
                print_(board)
        else:
            print('opps ! loss the toss \n \n your sign is 1')

            while True :
                
                try:
                    random_pos = choice_board[np.random.choice(index[(board==-1).flatten()])]
                except:
                    random_pos=None
                if random_pos is None:
                    break
                board = choose(board,random_pos,0)
                print_(board)
                
                while True:
                    choice_pos = int(input('Choose a position on board (0-8)'))
                    if choice_pos in index[(board==-1).flatten()]:
                        choice_pos = choice_board[choice_pos]
                        break
                    print('Choose again retard ')
                board = choose(board,choice_pos,1)
                
                print_(board)
                if not np.any((board==-1)):
                    print('zook')
                    break
        
        play_again = int(input('wanna play again'))
        if not play_again:
            break
play(board,weights,choice_board,index)
            