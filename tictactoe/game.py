import numpy as np

weights = np.zeros((9,9))
selection_times = np.zeros((9,9))
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

def update_weights(weights,board,sign):
    pass 





def check_result(board,sign):
    if board[0][0] == sign:
        if board[0][1]== sign:
            if board[0][2] == sign:
                return True
        if board[1][0] == sign:
            if board[2][0] == sign:
                return True
        if board[1][1] == sign:
            if board[2][2] == sign:
                return True
    if board[2][2] == sign:
        if board[2][1] == sign:
            if board[2][0] == sign:
                return True
        if board[1][2] == sign:
            if board[0][2]== sign:
                return True
    if board[1][1] == sign:
        if board[1][0] == sign:
            if board[1][2] == sign:
                return True
        if board[0][1] == sign:
            if board[2][1] == sign:
                return True
        if board[0][2] == sign:
            if board[2][0] == sign:
                return True
    return False




def play(choice_board,index):
   
    while True :
        board = -1*np.ones((3,3),dtype='int32')
        toss_input = int(input('choose Head(0) or Tail(1)'))
        toss = np.random.choice([0,1])
        if toss_input == toss:
            print('congrats you won the toss ! \n \n your sign is 0')
            while True:
                if  np.all((board!=-1)):
                    
                    break
               
                while True:
                    choice_pos = int(input('Choose a position on board (0-8)'))
                    if choice_pos in index[(board==-1).flatten()]:
                        choice_pos = choice_board[choice_pos]
                        break
                    print('Choose again retard ')
                board = choose(board,choice_pos,0)
                print_(board)
                if check_result(board,0):
                    print("yay! you won")
                    break
                try:
                    random_pos = choice_board[np.random.choice(index[(board==-1).flatten()])]
                except:
                    random_pos=None
                if random_pos is None:
                    break
                board = choose(board,random_pos,1)
                print_(board)
                if check_result(board,1):
                    print("you lose")
                    break
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
                if check_result(board,0):
                    print("you lose ")
                    break
                if np.all((board!=-1)):
                    break
                while True:
                    choice_pos = int(input('Choose a position on board (0-8)'))
                    if choice_pos in index[(board==-1).flatten()]:
                        choice_pos = choice_board[choice_pos]
                        break
                    print('Choose again retard ')
                board = choose(board,choice_pos,1)
                
                print_(board)
                if check_result(board,1):
                    print("yay! you won")
                    break
                
        
        play_again = int(input('wanna play again'))
        if not play_again:
            break
play(choice_board,index)
            