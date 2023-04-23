import time
import random
import copy
import numpy as np

#Grids 1-4 are 2x2
grid1 = [
        [1, 0, 4, 2],
        [4, 2, 1, 3],
        [2, 1, 3, 4],
        [3, 4, 2, 1]]

grid2 = [
        [1, 0, 4, 2],
        [4, 2, 1, 3],
        [2, 1, 0, 4],
        [3, 4, 2, 1]]

grid3 = [
        [1, 0, 4, 2],
        [4, 2, 1, 0],
        [2, 1, 0, 4],
        [0, 4, 2, 1]]

grid4 = [
        [1, 0, 4, 2],
        [0, 2, 1, 0],
        [2, 1, 0, 4],
        [0, 4, 2, 1]]

grid5 = [
        [1, 0, 0, 2],
        [0, 0, 1, 0],
        [0, 1, 0, 4],
        [0, 0, 0, 1]]

grid6 = [
        [0, 0, 6, 0, 0, 3],
        [5, 0, 0, 0, 0, 0],
        [0, 1, 3, 4, 0, 0],
        [0, 0, 0, 0, 0, 6],
        [0, 0, 1, 0, 0, 0],
        [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section, n):

    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
        return True
    return False

def get_squares(grid, n_rows, n_cols):

    squares = []
    for i in range(n_cols):
        rows = (i*n_rows, (i+1)*n_rows)
        for j in range(n_rows):
            cols = (j*n_cols, (j+1)*n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square +=line
            squares.append(square)


    return(squares)

#To complete the first assignment, please write the code for the following function
def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved

    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows*n_cols
    for line in grid:
        if check_section(line, n) == False:
            return False

    for i in range(n_rows**2):
        column = []
        for row in grid:
            column.append(row[i])

        if check_section(column, n) == False:
            return False

    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False

    return True


def find_empty(grid):
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None

    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)

    return None

def empty_cell_list(board):
    '''

    Parameters
    ----------
    board : TYPE           nested list
            DESCRIPTION.   unfinished suduko grid displayed as a nested list

    Returns
    -------
    empties : TYPE         nested list
        DESCRIPTION        list of coordinates for the empty spaces in board

    '''

    # iterates across the passed board and returns the position vector of any empty spaces

    position = 0
    empties = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                empties.append([])  # adds an empty slot to the nested list
                empties[position].extend([row, col])  # fills that empty slot with a coord
                position = position + 1

    return empties

# print(empty_cell_list(grid4))

def poss(grid, n_rows, n_cols,i,j):

    '''returns a list of viable values for empty spaces in the grid based on the values already present in the row,column and subgrid.
    Takes the same arguments as recursive_solve() and also i,j which is the location of the empty space that is being operated on.
    This i, j is the output of the find_empty() function.'''

    length = len(grid)
    # creating a nested list for each subgrid in the grid, uses the fact that the nuber of subgrids is equal to the number of elements in one direction.
    subgrids = [[] for list in range(length)]
    # Uing n_rows and n_cols provided as division lines for the subgrids in the grid.
    gridline_y = n_rows
    gridline_x = n_cols
    #iterating across each element to assign it to a nested list for its subgrid
    for row in range(0, length):
        # Using gridlines to assign a 'sub x and y index' to the elements based on their location:
        # e.g. for grid1 (2x2) elements on the left of gridline get sub x index 0 (0//2 = 1//2 = 0)
        # and on the right of the  gridline they get sub x index 1. The same applies to the vertical gridline.
        sub_Y_ind = row // gridline_y
        for col in range(0, length):
            sub_X_ind = col // gridline_x

            # Used trial and error to find this formula, It uses the sub x index and sub y index of the element to build a number
            # corresponding to an index for the nested lists in the subgrid.
            # E.g. for top left subgrid in grid sub_x_ind = sub_y_ind = 0 so then sub_num = 0.
            # for bottom left subgrid: sub_x_ind = 0, sub_y_ind = 1 so sub_num = 2*1 + 0 = 2.
            # So the elements in the first and third subgrids go into the first and third nested list.

            sub_num = gridline_y * sub_Y_ind + sub_X_ind
            subgrids[sub_num].append(grid[row][col])

    # Using the formula used above to find the index of the subgrid of the empty space in question
    sub_partic = gridline_y * (i // gridline_y) + (j // gridline_x)
    # Building lists of values in the same row, column and subgrid of the empty space in question.
    neigh_col = [grid[k][j] for k in range(0, len(grid))]
    neigh_row = grid[i]
    neigh_sub = subgrids[sub_partic]
    neighbours = neigh_col + neigh_row + neigh_sub
    # Building a list of viable values for the empty space in question.
    viable = [x for x in range(0,len(grid)+1) if x not in neighbours]
    return viable

def min(grid,n_rows,n_cols):
    '''

    Inputs:
        grid, dimensions.

    Returns:
        A list of lists, sorted by length, each of which contains
        the row and column of the empty cell in question as the first
        two elements and then all possible numbers for that element.
    '''

    # Creating adding the possible numbers to the empty cell list to create
    # 'hybrid' lists.
    empties = empty_cell_list(grid)
    for i in empties:
        for j in poss(grid,n_rows,n_cols,i[0],i[1]):
            i.append(j)
    # sorting the hybrid nested lists by length
    empties.sort(key=len)
    return empties

def find_min_remaining_values(board):
    '''
    
    Parameters
    ----------
    board : TYPE
        DESCRIPTION.
    Returns
    -------
    min_row : TYPE
        DESCRIPTION.
    min_col : TYPE
        DESCRIPTION.
    '''
    #uses the list of empty slots from the empty_cell_list function and the find_possible_values function (seperate file) to find the values
    #each empty slot can hold 
    #then returns the slot with the least possible values 
    
    
    min_remaining_values = len(board) + 1 #sets the maximum values possible 
    min_row, min_col = None, None #if min_row and min_col stay as none then the grid is complete
    empties = empty_cell_list(board)
    for i in range(len(empties)):
        remaining_values = len(find_possible_options(board, empties[i][0], empties[i][1]))
        if remaining_values < min_remaining_values:
            remaining_values = min_remaining_values
            min_row, min_col = empties[i][0], empties[i][1]
    
    
    return min_row, min_col

def remove_same_poss(poss_vals, value):
    for val in poss_vals:
        if val == value:
            poss_vals.remove(val)


def same_square_check (row_ind, col_ind, n_rows, n_cols):
    col_sect = col_ind/n_cols #if division is a float 
    row_sect = row_ind/n_rows
    col_n = col_ind//n_cols #if division is a wole number/ int 
    row_n = row_ind//n_rows
    if type(col_sect) == float:
        col_interval = [col_n, col_n+1] 
    if type (col_sect) == int:
        col_interval = [col_sect-1, col_sect]
    if type(row_sect) == float:
        row_interval = [row_n, row_n+1]
    if type(row_sect) ==int:
        row_interval = [row_sect-1, row_sect]
    #col_interval = [col_sect, col_sect+1]
    #row_interval = [row_sect, row_sect+1]
    return [row_interval, col_interval]


def wavefront(grid, n_rows, n_cols):
    #check that there are empty spaces in the grid:
    empty = find_empty(grid)
    if not empty:#### and is_solved(grid):
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            return None 
    #identify and list the coordinates of each empty cell in the grid -> [row,col] of empty cells
    empty_cells = empty_cell_list(grid)
    # print(empty_cells)
    ##calculates the possible values for each empty cell in the grid, returns the grid with all possible values of unknown cells listed
    ##replaces the unknown cells with a list of possible values for that position 
    empty_cells_in_order = min(grid, n_rows, n_cols) #returns the (row, col, possible_vals) for each empty space, in order of number of possibilities 
    # print(empty_cells_in_order)
    for i in empty_cells_in_order:
       # print(i) #to check 
        grid[i[0]][i[1]] = i[2:]   #replces the '0' representing an empty cell with all the possible values for that empty cell
    #print(grid)
    #print(empty_cells_in_order)
    ####cell_with_multiple_opts = []
    for i in empty_cells_in_order:  #for the number of items in the list of 'Empty_cells' - so for each empty cell listed
        #run the recursive solve function, except: 
        #-the cells are approached in order of the number of possible values
        #-once the right value of the cell is found, remove that possible value from other unknown cells in the same row or column
        ###1 if the cell has only one possible value 
        #input(i)
        if len(grid[i[0]][i[1]]) == 1:
        #replace the value of the cell with the only possible value:
            grid[i[0]][i[1]] = i[2]
            #remove the cell from the list of empty cells (as it has to be that value) - list then becomes a list of cells with more than one possible value
    #    print(np.array(grid)) 
        ####if is_solved(grid):
          ####  return grid
        ####else:
            #### wavefront(grid,n_rows,n_cols)
           # print (' The row value of the empty cell iterating through i[0]:', i[0])
            for j in empty_cells_in_order: #for each cell listed in empty grid list 
            #    print('The row value of all cells listed under empty_cells list j[0]:', j[0])
                if len(j)>3: #if the cell has more than one possible value 
                    if j[0] == i[0]: #if the cell has the same row value
            ###NEED TO ONLY ACCESS THE ELEMENTS AFTER THE FIRST TWO ELEMENTS IN A GRID
                        for poss_val in grid[j[0]][j[1]]:
                       #     print ('possible value:', poss_val)
                        #    print ('value to remove:', i[2])
                         #   print ('all poss vals(listed in grid):', grid[j[0]][j[1]])
                            if poss_val == i[2]:
                                remove_same_poss(grid[j[0]][j[1]], i[2])
                                
                                print('1', grid[j[0]][j[1]])
                                # grid[j[0]][j[1]].remove(i[2])
                                #remove the cells new value from the list of potential cells for other cells in the same row
		    #isolate the column index and equate to i[2]
                    if j[1] == i[1]: #if the cell has the same column value
                        for poss_val in grid[j[0]][j[1]]:
                            if poss_val == i[2]:
                                remove_same_poss(grid[j[0]][j[1]], i[2])
                                print('2', grid[j[0]][j[1]])

            #identify the cells in the same square as the cell and equate to i[2]
                #if the column section of the two values are the same:
                    square_int_i = same_square_check (i[0], i[1], n_rows, n_cols) #gives the square i is in 
                    square_int_j = same_square_check (j[0], j[1], n_rows, n_cols) # give the square j is in 
                    if square_int_i == square_int_j:
                        for poss_val in grid[j[0]][j[1]]:
                            if poss_val == i[2]:
                                remove_same_poss(grid[j[0]][j[1]], i[2]) 
                                print('3', grid[j[0]][j[1]])
               # print ('after removing:',i[2], ', from poss vals, grid:', grid[j[0]][j[1]])
                #print (grid)
                if len(grid[i[0]][i[1]]) == 1:
                    #replace the value of the cell with the only possible value:
                    grid[i[0]][i[1]] = i[2]
            print ('new grid:', np.array(grid))
                ##      grid[j[0]][j[1]].remove(i[2])
          #  print (empty_cells_in_order)
   # wavefront(grid, n_rows, n_cols)      
    #1print (np.array(grid))



#def is_solved(grid):
    # Check if there is any lists left instead of an int
 #   solved = 
  #  return True if solved else False

wavefront(grid5, 2, 2)

