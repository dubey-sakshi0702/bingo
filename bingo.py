import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
def change_player(player):
    if player=='Player 1':
        return 'Player 2'
    else:
        return 'Player 1'
def get_board():
    b = []
    for i in range(0, 24):
        ele = input()
        b.append(ele) # adding the element
        if int(b[x])<10:
            b[x]=' '+b[x]

def board_input(board):
    i=0
    while i not in [1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] and not board[i]=='X':
        i=int(input('enter a no 1 to 25\n'))
    return i 
    

def display_board(board):

    print('    |    |    |    |')
    print(' ' + board[20] + ' | ' + board[21] + ' | ' + board[22] + ' | ' + board[23] + ' | ' + board[24])
    print('    |    |    |    |')
    print('----------------------')
    print('    |    |    |    |')
    print(' ' + board[15] + ' | ' + board[16] + ' | ' + board[17] + ' | ' + board[18] + ' | ' + board[19])
    print('    |    |    |    |')
    print('----------------------')
    print('    |    |    |    |')
    print(' ' + board[10] + ' | ' + board[11] + ' | ' + board[12] + ' | ' + board[13] + ' | ' + board[14]) 
    print('    |    |    |    |')
    print('----------------------')
    print(' ' + board[5] + ' | ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |    |    |    |')
    print('----------------------')
    print('    |    |    |    |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4]) 
    print('    |    |    |    |')
def win(board):
    mark='X'
    c=0
    if(board[0] == mark and board[1] == mark and board[2] == mark and board[3] == mark and board[4]):
        c+=1  
    if(board[5] == mark and board[6] == mark and board[7] == mark and board[8] == mark and board[9]):
        c+=1
    if(board[10] == mark and board[14] == mark and board[11] == mark and board[12] == mark and board[13]): 
        c+=1
    if(board[15] == mark and board[16] == mark and board[17] == mark and board[18] == mark and board[19]) :
        c+=1
    if(board[21] == mark and board[20] == mark and board[23] == mark and board[24] == mark and board[22])  :
        c+=1
    if(board[20] == mark and board[10] == mark and board[5] == mark and board[0] == mark and board[15]) :
        c+=1
    if(board[21] == mark and board[16] == mark and board[11] == mark and board[6] == mark and board[1])  :
        c+=1
    if(board[12] == mark and board[22] == mark and board[17] == mark and board[7] == mark and board[2])  :
        c+=1
    if(board[18] == mark and board[13] == mark and board[23] == mark and board[8] == mark and board[3])  :
        c+=1
    if(board[14] == mark and board[19] == mark and board[9] == mark and board[24] == mark and board[4])  :
        c+=1
    if(board[12] == mark and board[20] == mark and board[16] == mark and board[8] == mark and board[4]) :
        c+=1
    if(board[18] == mark and board[12] == mark and board[3] == mark and board[6] == mark and board[0])  :
        c+=1
    if(c>=5):
        return True
    
    else:
        return False
def crossing( b1,b2,ele):
    ind1=b1.index(ele)
    b1[ind1]='X'
    ind2=b1.index(ele)
    b2[ind2]='X'
print('welcome to bingo')
t=input('want to play?(enter y/Y to play)')
if t=='y' or t== 'Y':
    print("welcome players\n\n\n ")
    player=choose_first()
    b1=get_board()
    player=change_player(player)
    b2=get_board()
    for i in range(0,24):
        player=change_player()
        display_board(b1)
        print(player)
        i=board_input(b1)
        crossing(b1,b2,i)
        if win(b1)==True:
            print(f'{player} won')
            display_board(b1)
            print(f"{player}'s board")
            print('\n'*5)
            change_player(player)
            display_board(b2)
            print(f"{player}'s board")
            break
        elif win(b2)==True:
            change_player(player)
            display_board(b2)
            print(f"{player}'s board")
            change_player(player)
            display_board(b1)
            print(f"{player}'s board")
            break
        else:
            print('\n'*50)
            change_player(player)
            display_board(b1)
            print(f"{player}'s board")
            i=board_input(b1)
        crossing(b1,b2,i)
        if win(b2)==True:
            print(f'{player} won')
            display_board(b1)
            print(f"{player}'s board")
            print('\n'*5)
            change_player(player)
            display_board(b2)
            print(f"{player}'s board")
            break
        elif win(b1)==True:
            change_player(player)
            display_board(b2)
            print(f"{player}'s board")
            change_player(player)
            display_board(b1)
            print(f"{player}'s board")
            break
        else:
            print('\n'*50)






  
    
  


