"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


    
            
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    no_x=0
    no_O=0   
    for i in board:
        nested_list=i
        no_x = no_x + nested_list.count('X')
        no_O=no_O + nested_list.count('O')
    if no_x > no_O:
        return O
    else:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=set()

    for i in range(len(board)):
        #print(board[i])
        nested_list=board[i]
        for j in range(len(nested_list)):
            if nested_list[j]==None:
                sub_action=(i,j)
                #print(sub_action)
                actions.add(sub_action)
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    board2=copy.deepcopy(board)
    new_move=action
    old_move=board2[new_move[0]][new_move[1]]
    #print(old_move)
        
    if old_move == None:
        
        if player(board2)=='X':
            board2[new_move[0]][new_move[1]]='X'            
        else:
            board2[new_move[0]][new_move[1]]='O'
        
        return board2
    else:
        raise Exception("Action is invalid")

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if terminal(board)==True:
        winner=final(board)
        return winner[1]
    else:
        return 'Game not over'
        
        
                
    raise NotImplementedError

def final(board):
    diagonal_list=[]
    diagonal_list2=[]
    for i in range(len(board)):
            #print(board[i])
            vertical_list=[]
            horizontal_list=[]
            diagonal_element=board[i][i]
            diagonal_element2=board[i][2-i]
            diagonal_list.append(diagonal_element)
            diagonal_list2.append(diagonal_element2)
            for j in range(len(board)):
                vertical_element=board[j][i]
                horizontal_element=board[i][j]
                vertical_list.append(vertical_element)
                horizontal_list.append(horizontal_element)
            if vertical_list[0]==vertical_list[1]==vertical_list[2]!=None:
                return True,vertical_list[0]
            elif horizontal_list[0]==horizontal_list[1]==horizontal_list[2]!=None:
                return True,horizontal_list[0]
    if diagonal_list[0]==diagonal_list[1]==diagonal_list[2]!=None:
        return True,diagonal_list[0]
    elif diagonal_list2[0]==diagonal_list2[1]==diagonal_list2[2]!=None:
        return True,diagonal_list2[0]
    elif actions(board)==set():
            return True,None
    else:
        return False,None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    starting=initial_state()
    
    
    if (board==starting):
        return False
    else:
        test=final(board)
        #print(test)
        return(test[0])
        
        
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    whowin=winner(board)
    #print('winner is' ,whowin)
    
    if whowin=='X':
        return 1
    elif whowin=='O':
        return -1
    elif whowin==None:
        return 0
    else:
        return 'Game Not over'
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board)==True:
        return None

    playerturn=player(board)
    #print(playerturn)
    allaction=actions(board)
    results_board=[]
    state_val=[]    
    #print(allaction)
    state_dict={}
    i=1
    for action in allaction:
        result_state=result(board,action)
        state_dict[i] = {}
        state_dict[i]['result']=result_state
        state_dict[i]['action']=action
        print('this actions',action,' yields',result_state)
        i=i+1
    ##print(state_dict,'\n')

    if playerturn=='X':
        optimum_state=float('-Inf')
        for i in state_dict:
            ##print('index number is',i)
            resultedstate=state_dict[i]['result']
            ##print('For resulted state',resultedstate)
            state_value=Min_value(resultedstate,results_board,state_val)
            state_dict[i]['value']=state_value
            #print('statevalue is',state_value)
            ##print('action is',state_dict[i]['action'],'\n')
            #n=state_dict[i]['value']
            if state_value>optimum_state:
                optimum_state=state_value
                ##print('stateval is ',optimum_state)
                optimum_action=state_dict[i]['action']
        return optimum_action
        
    elif playerturn=='O':
        optimum_state=float('Inf')
        for i in state_dict:
            ##print('index number is',i)
            resultedstate=state_dict[i]['result']
            ##print('For resulted state',resultedstate)
            state_value=Max_value(resultedstate,results_board,state_val)
            state_dict[i]['value']=state_value
            ##print('statevalue is',state_value)
            ##print('action is',state_dict[i]['action'],'\n')
            #n=state_dict[i]['value']
            if state_value<optimum_state:
                optimum_state=state_value
                ##print('stateval for index',i,'is ',optimum_state)
                optimum_action=state_dict[i]['action']
        return optimum_action  
            
    raise NotImplementedError

def Max_value(board,results_board,state_val):
    ##print('\n','In max value ','\n all actions are',actions(board),'\n for board',board,'\n')
    if board in results_board:
        ##print('Max Val top if')
        n=results_board.index(board)
        return state_val[n]

    elif terminal(board)==True:
        results_board.append(board)
        state_val.append(utility(board))   
        return utility(board)
    else:
        n_infinity = float('-Inf')
        ##print('n_infinity',n_infinity)
        for action in actions(board):
            ##print('inside max_val function has action',action)
            ##print('Maxvalue called','\n',board,'\n')
            childstate=Min_value(result(board,action),results_board,state_val)
            n_infinity=max(n_infinity,childstate)
        print('Finish looping n_inf=',n_infinity)    
        results_board.append(board)
        state_val.append(n_infinity)
        return n_infinity

    raise NotImplementedError

def Min_value(board,results_board,state_val):
    """
    find the value of the state where player is trying to minimize the value
    """
    #print(terminal(board))
    #print(utility(board))
    ##print('\n','In min value ','\n all actions are',actions(board),'\n for board',board,'\n')
    if board in results_board:
        ##print('Min Val top if')
        n=results_board.index(board)
        return state_val[n]
    elif terminal(board)==True:
        results_board.append(board)
        state_val.append(utility(board)) 
        return utility(board)
    else:
        p_infinity = float('Inf')
        ##print('p_infinity',p_infinity)
        for action in actions(board):
            childstate=Max_value(result(board,action),results_board,state_val)
            ##print('inside min_val function has action',action)
            ##print('Minvalue called','\n',board,'\n')
            p_infinity=min(p_infinity,childstate)
        print('Finish looping p_inf=',p_infinity)
        results_board.append(board)
        state_val.append(p_infinity)
        return p_infinity
