#from Ipython.display import clear_output
def display_board(list1):
   # clear_output
    print(list1[0]+'|'+list1[1]+'|'+list1[2])
    print(list1[3] + '|' + list1[4]+'|'+list1[5])
    print(list1[6] + '|' + list1[7]+'|'+list1[8])
def player_input():
    player_choose1=''
    player2=''
    while player_choose1 not in ('X','O'):
       player_choose1=input("Player 1:Do you want to be X  or O ?: ")

    if(player_choose1=='X'):
        player2='O'
    else:
        player2='X'
    return player_choose1,player2

def choose_position(player1,player2,list1):
    pos1=''
    pos2=' '
    while pos1 not in range(0,9) or pos2 not in range(0,9):
       pos1=int(input(f'Player 1:Choose an index position for player between 0-8:'))
       if pos1 in range(0,9):
         list1[pos1]=player1
         pos2 = int(input(f'Player 2:Choose an index position for player between 0-8:'))
         if pos2 in range(0,9):
           list1[pos2]=player2






print("Welcome to the Tic Tac Toe!")
list1=['','','','','','','','','']
display_board(list1)
player1,player2=player_input()
print(f'Player 1: {player1}')
print(f'Player 2: {player2}')
choose_position(player1,player2,list1)
display_board(list1)



