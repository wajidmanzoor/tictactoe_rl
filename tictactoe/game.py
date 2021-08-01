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

def choose(board,weights,index,choice_board,t,selection_times,pos=None,sign=0,bot= False,c=0.1):
    if not bot:
        board[pos[0]][pos[1]]=sign
    else:
        row = np.sum((board==-1).flatten())-1
        actions = index[(board==-1).flatten()]

        temp = np.argmax(weights[row,:][actions]+c*np.sqrt((np.log(t)/(selection_times[row,:][actions]+1))))
        action = actions[temp]
        #board[choice_board[action][0],choice_board[action][1]] = sign
        return action

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



#board,weights,index,choice_board,t,selection_times,pos=None,sign=0,bot= False,c=0.1
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
#play(choice_board,index,weights)






def train(choice_board,index,weights,t,selection_times,bot=(True,True),c=0.1):
   
    df = pd.DataFrame(columns =['bot','0','1','2','3','4','5','6','7','8'])
    board = -1*np.ones((3,3),dtype='int32')
    #toss_input = int(input('choose Head(0) or Tail(1)'))
    toss = np.random.choice([0,1])
    if toss:
        #print('Bot 1 won the toss ! \n \n your sign is 0')
        while True:
            if  np.all((board!=-1)):
                break
            row1 = np.sum((board==-1).flatten())-1
            try:
                ind = choose(board,weights,index,choice_board,t,selection_times,sign=0,bot=True,c=c)
                pos = choice_board[ind]
                board[pos[0],pos[1]] = 0
                selection_times[row1,:][ind] += 1
                df.loc[len(df)] = [1]+list(board.flatten())
            except:
                pos = None
            if pos is None:
                break
            #print_(board)
            update = update_weights(board,choice_board,0,ind)
            #print(update)
            weights[row1,:][ind] += update
            if check_result(board,0):
                weights[row1,:][ind] += 10
                weights[row2,:][ind] -= 10
                #print_(board)
                #print("bot 1 won")
                break
            row2 = np.sum((board==-1).flatten())-1
            try:
                ind = choose(board,weights,index,choice_board,t,selection_times,sign=1,bot=True,c=c)
                pos = choice_board[ind]
                board[pos[0],pos[1]] = 1
                selection_times[row2,:][ind] += 1
                df.loc[len(df)] = [2]+list(board.flatten())
            except:
                pos = None
            if pos is None:
                break
            update = update_weights(board,choice_board,1,ind)
            #print(update)
            weights[row2,:][ind] += update
            #print_(board)
            if check_result(board,1):
                weights[row1,:][ind] -= 10
                weights[row2,:][ind] += 10
                #print_(board)
                #print("bot 2 won ")
                break
    else:
        #print('Bot 2 won the toss ! \n \n your sign is 0')

        while True :
            
            if  np.all((board!=-1)):
                return weights,selection_times

            row1 = np.sum((board==-1).flatten())-1
            try:
                ind = choose(board,weights,index,choice_board,t,selection_times,sign=1,bot=True,c=c)
                pos = choice_board[ind]
                board[pos[0],pos[1]] = 1
                selection_times[row1,:][ind] += 1
                df.loc[len(df)] = [2]+list(board.flatten())
            except:
                pos = None
            if pos is None:
                break

            
            #print(ind)
            update = update_weights(board,choice_board,1,ind)
            #print(update)
            weights[row1,:][ind] += update
            #print_(board)
            if check_result(board,1):
                weights[row1,:][ind] += 10
                weights[row2,:][ind] -= 10
                #print_(board)
                #print("bot 2 won")
                break

            row2 = np.sum((board==-1).flatten())-1
            try:
                ind = choose(board,weights,index,choice_board,t,selection_times,sign=0,bot=True,c=c)
                pos = choice_board[ind]
                
                board[pos[0],pos[1]] = 0
                selection_times[row2,:][ind] += 1
                df.loc[len(df)] = [1]+list(board.flatten())
            except:
                pos = None
            if pos is None:
                break

            update = update_weights(board,choice_board,0,ind)
            #print(update)
            weights[row2,:][ind] += update
            #print_(board)
            if check_result(board,0):
                weights[row1,:][ind] -= 10
                weights[row2,:][ind] += 10
                #print_(board)
                #print("bot 1 won ")
                break
    df.to_csv('result/result'+str(t)+'.csv')
    return weights,selection_times

  
import pandas as pd
for i in range(1,10000):
    weights,selection_times =  train(choice_board,index,weights,i,selection_times)


df = pd.DataFrame(weights)
df1 = pd.DataFrame(selection_times)
df.to_csv('weights.csv')
df1.to_csv('selection_times.csv')