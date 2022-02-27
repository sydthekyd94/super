import copy #used for deepcopy of nested lists (matrices)
import numpy #used for showing the map in matrix form.
import os #used for clear console
import msvcrt #for not requiring enter

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def move(move,my_list):
    valid_moves = ['W','A','S','D']
    update_list = copy.deepcopy(my_list) #make a copy of the argument list
    max_row_index = len(update_list) - 1 #this is border
    max_col_index = len(update_list[0]) - 1 #this is border
    max_row_move = max_row_index - 1 #this is the farthest down you can travel
    max_col_move = max_col_index - 1 #this is the farthest right you can travel
    try: #assert map is a matrix, and just return the original map value if not. 
        assert type(my_list) is list
        for y in my_list:
            assert type(y) is list
    except (AssertionError):
        print("Map is not valid!")
    try: #assert move is in WASD then apply move if valid, otherwise return original map value if not
        assert move in valid_moves
    #assert my_list is a nested list
        for y in my_list: #for each row in list
            row = my_list.index(y) #this is the row #, with 0 being top most row
            for x in my_list[row]: #for each column in current row
                column = my_list[row].index(x) #this is column #, with 0 being leftmost row
                if my_list[row][column] == 0: #if current cell = 0
                    current_column = column #set index of column to be current index
                    current_row = row #set index of row to be current row 
                    if move == 'W': #up
                        if current_row != 1:
                            new_row = current_row - 1 #set new row to be 1 above current
                        else:
                            new_row = current_row
                    elif move == 'S': #down
                        if current_row != max_row_move:
                            new_row = current_row + 1 #set new row to be 1 below current
                        else:
                            new_row - current_row
                    elif move == 'A': #left
                        if current_column != 1:
                            new_column = current_column - 1 #set new column to be 1 left from current
                        else:
                            new_column = current_column
                    else: #right
                        if current_column != max_col_move:
                            new_column = current_column + 1 #set new column to be 1 right from current
                        else:
                            new_column = current_column
        #if move in valid_moves:
        update_list[current_row][current_column] = 1 #replace old value (moved from) to 1
        if move == 'W' or move == 'S': #moving up or down
            update_list[new_row][current_column] = 0 #replace new value (moved to) to 0
        else: #moving left or right
            update_list[current_row][new_column] = 0 #replace new value (moved to) to 0
    except (AssertionError):
        print("That\'s not a valid move!")
    finally:
        return update_list #return the new list

no_quotes = {39:None}
#big_map = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,0,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
big_map = [['X','X','X','X','X','X','X','X'],['X',1,1,1,1,1,1,'X'],['X',1,1,1,1,0,1,'X'],['X',1,1,1,1,1,1,'X'],['X',1,1,1,1,1,1,'X'],['X',1,1,1,1,1,1,'X'],['X',1,1,1,1,1,1,'X'],['X','X','X','X','X','X','X','X']]
while True:
    print("""
    Use W to move!
       ASD
    Press P to quit""")
    formatted_map = str(numpy.array(big_map)).replace(' [','').replace('[','').replace(']','').replace('1',' ')
    print(formatted_map.translate(no_quotes))
    #user_input = input().upper()
    user_input = msvcrt.getch().decode('ASCII').upper()
    if user_input == "P":
        break

    else:
        big_map = move(user_input,big_map)
        clearConsole()
      
