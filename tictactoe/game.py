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
        for j in board[i,:]:
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

def update_weights(board,choice_board,sign,ind):
    update = 0
    if ind == 1 or ind == 7:
        if board[choice_board[ind-1][0],choice_board[ind-1][1]] == sign and board[choice_board[ind+1][0],choice_board[ind+1][1]] == -1:
            update +=1
        elif board[choice_board[ind-1][0],choice_board[ind-1][1]] == -1 and board[choice_board[ind+1][0],choice_board[ind+1][1]] == sign:
            update +=1
        if ind ==1:
            if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[7][0],choice_board[7][1]] == -1:
                update +=1
            elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[7][0],choice_board[7][1]] == sign:
                update +=1
        elif ind ==1:
            if board[choice_board[4][0],choice_board[4][0]] == sign and board[choice_board[1][0],choice_board[1][0]] == -1:
                update +=1
            elif board[choice_board[4][0],choice_board[4][0]] == -1 and board[choice_board[1],choice_board[1][0]] == sign:
                update +=1
    elif ind == 3 or ind == 5:
        if board[choice_board[ind-3][0],choice_board[ind-3][1]] == sign and board[choice_board[ind+3][0],choice_board[ind+3][1]] == -1:
            update +=1
        elif board[choice_board[ind-3][0],choice_board[ind-3][1]] == -1 and board[choice_board[ind+3][0],choice_board[ind+3][1]] == sign:
            update +=1
        if ind ==3:
            if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[5][0],choice_board[5][1]] == -1:
                update +=1
            elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[5][0],choice_board[5][1]] == sign:
                update +=1
        elif ind ==5:
            if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[3][0],choice_board[3][1]] == -1:
                update +=1
            elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[3][0],choice_board[3][1]] == sign:
                update +=1
    elif ind == 0:
        if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[8][0],choice_board[8][1]] == -1:
            update +=1
        elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[8][0],choice_board[8][1]] == sign:
            update +=1
        if board[choice_board[ind+1][0],choice_board[ind+1][1]] == sign and board[choice_board[ind+2][0],choice_board[ind+2][1]] == -1:
            update +=1
        elif board[choice_board[ind+1][0],choice_board[ind+1][1]] == -1 and board[choice_board[ind+2][0],choice_board[ind+2][1]] == sign:
            update +=1
        if board[choice_board[ind+3][0],choice_board[ind+3][1]] == sign and board[choice_board[ind+6][0],choice_board[ind+6][1]] == -1:
            update +=1
        elif board[choice_board[ind+3][0],choice_board[ind+3][1]] == -1 and board[choice_board[ind+6][0],choice_board[ind+6][1]] == sign:
            update +=1
    elif ind == 2:
        if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[6][0],choice_board[6][1]] == -1:
            update +=1
        elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[6][0],choice_board[6][1]] == sign:
            update +=1
        if board[choice_board[ind-1][0],choice_board[ind-1][1]] == sign and board[choice_board[ind-2][0],choice_board[ind-2][1]] == -1:
            update +=1
        elif board[choice_board[ind-1][0],choice_board[ind-1][1]] == -1 and board[choice_board[ind-2][0],choice_board[ind-2][1]] == sign:
            update +=1
        if board[choice_board[ind+3][0],choice_board[ind+3][1]] == sign and board[choice_board[ind+6][0],choice_board[ind+6][1]] == -1:
            update +=1
        elif board[choice_board[ind+3][0],choice_board[ind+3][1]] == -1 and board[choice_board[ind+6][0],choice_board[ind+6][1]] == sign:
            update +=1
    elif ind == 6:
        if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[2][0],choice_board[2][1]] == -1:
            update +=1
        elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[2][0],choice_board[2][1]] == sign:
            update +=1
        if board[choice_board[ind+1][0],choice_board[ind+1][1]] == sign and board[choice_board[ind+2][0],choice_board[ind+2][1]] == -1:
            update +=1
        elif board[choice_board[ind+1][0],choice_board[ind+1][1]] == -1 and board[choice_board[ind+2][0],choice_board[ind+2][1]] == sign:
            update +=1
        if board[choice_board[ind-3][0],choice_board[ind-3][1]] == sign and board[choice_board[ind-6][0],choice_board[ind-6][1]] == -1:
            update +=1
        elif board[choice_board[ind-3][0],choice_board[ind-3][1]] == -1 and board[choice_board[ind-6][0],choice_board[ind-6][1]] == sign:
            update +=1
    elif ind == 8:
        if board[choice_board[4][0],choice_board[4][1]] == sign and board[choice_board[0][0],choice_board[0][1]] == -1:
            update +=1
        elif board[choice_board[4][0],choice_board[4][1]] == -1 and board[choice_board[0][0],choice_board[0][1]] == sign:
            update +=1
        if board[choice_board[ind-1][0],choice_board[ind-1][1]] == sign and board[choice_board[ind-2][0],choice_board[ind-2][1]] == -1:
            update +=1
        elif board[choice_board[ind-1][0],choice_board[ind-1][1]] == -1 and board[choice_board[ind-2][0],choice_board[ind-2][1]] == sign:
            update +=1
        if board[choice_board[ind-3][0],choice_board[ind-3][1]] == sign and board[choice_board[ind-6][0],choice_board[ind-6][1]] == -1:
            update +=1
        elif board[choice_board[ind-3][0],choice_board[ind-3][1]] == -1 and board[choice_board[ind-6][0],choice_board[ind-6][1]] == sign:
            update +=1
    elif ind == 4:
        if board[choice_board[ind-4][0],choice_board[ind-4][1]] == sign and board[choice_board[ind+4][0],choice_board[ind+4][1]] == -1:
            update +=1
        elif board[choice_board[ind-4][0],choice_board[ind-4][1]] == -1 and board[choice_board[ind+4][0],choice_board[ind+4][1]] == sign:
            update +=1
        if board[choice_board[ind-2][0],choice_board[ind-2][1]] == sign and board[choice_board[ind+2][0],choice_board[ind+2][1]] == -1:
            update +=1
        elif board[choice_board[ind-2][0],choice_board[ind-2][1]] == -1 and board[choice_board[ind+2][0],choice_board[ind+2][1]] == sign:
            update +=1
        if board[choice_board[ind-3][0],choice_board[ind-3][1]] == sign and board[choice_board[ind+3][0],choice_board[ind+3][1]] == -1:
            update +=1
        elif board[choice_board[ind-3][0],choice_board[ind-3][1]] == -1 and board[choice_board[ind+3][0],choice_board[ind+3][1]] == sign:
            update +=1
        if board[choice_board[ind-1][0],choice_board[ind-1][1]] == sign and board[choice_board[ind+1][0],choice_board[ind+1][1]] == -1:
            update +=1
        elif board[choice_board[ind-1][0],choice_board[ind-1][1]] == -1 and board[choice_board[ind+1][0],choice_board[ind+1][1]] == sign:
            update +=1
    update += 0.25
    return update
        
        



    





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




def play(choice_board,index,weights):
   
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
                    weights[row,:][ind] -= 10
                    print("yay! you won")
                    break
                try:
                    ind = np.random.choice(index[(board==-1).flatten()])
                    random_pos = choice_board[ind]
                except:
                    random_pos=None
                if random_pos is None:
                    break
                row = np.sum((board==-1).flatten())-1
                board = choose(board,random_pos,1)
                update = update_weights(board,choice_board,1,ind)
                print(update)
                weights[row,:][ind] += update
                print_(board)
                if check_result(board,1):
                    weights[row,:][ind] += 10
                    print("you lose")
                    break
        else:
            print('opps ! loss the toss \n \n your sign is 1')

            while True :
                
                try:
                    ind = np.random.choice(index[(board==-1).flatten()])
                    random_pos = choice_board[ind]
                except:
                    random_pos=None
                if random_pos is None:
                    break
                row = np.sum((board==-1).flatten())-1
                board = choose(board,random_pos,0)
                update = update_weights(board,choice_board,0,ind)
                weights[row,:][ind] += update 
                print_(board)
                if check_result(board,0):
                    weights[row,:][ind] += 10
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
                    weights[row,:][ind] -= 10
                    print("yay! you won")
                    break
                
        
        play_again = int(input('wanna play again'))
        if not play_again:
            print(weights)
            break
play(choice_board,index,weights)
            