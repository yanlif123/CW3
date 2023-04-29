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


def remove_same_poss(poss_vals, value):
    """
    If an element in the list 'poss_vals' is the same as the value inputted, remove the value from the list 

    Input:
        list name, value to check for and remove from list

    Return 
        list with the specific value removed
    """
    for val in poss_vals:
        if val == value:
            poss_vals.remove(val)


def same_square_check (row_ind, col_ind, n_rows, n_cols):
    """
    Returns the indices of the square the cell is in - is used to check if two cells are in the same square
    Input: 
        cell's row index, cell's column index, grid row dimensions, grid column dimensions
    
    Return:
        row index and column index of the square the cell is within 
    """
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
    return [row_interval, col_interval]


def wavefront(grid, n_rows, n_cols):
    """
    Task 3
    -This function replaces unknown cells in the grid with a list of the possible values for each cell.
    -The value of cells with only one possible value are then stored in the grid, and this value is 
     removed from lists of possible values for other unknown cells in the same row, column or section. 
    -This is repeated until either the grid is solved, or until there are no more unknown cells with only one possible value.
    If the latter occurs, the unknown cell with the least number of possible values is assigned a value by random, and the function 
    is called again, until the grid is solved.
    """
    """
    Inputs:
        grid, row dimensions, column dimensions

    Returns:
        solved grid of the grid inputted
    """

    #check if the grid is solved, return grid if solved
    if check_solution(grid, n_rows, n_cols) == True: 
        print ('final grid', np.array(grid))
        return np.array(grid)
    
    #find the empty cells of the grid inputted 
    empty_cells_in_order = min(grid, n_rows, n_cols) #returns the (row, col, possible_vals) for each empty space, in order of cell with least poss_vals
    
    #replace unsolved cells in grid (represented with a '0') with a list of possible values for that cell 
    for i in empty_cells_in_order:
        grid[i[0]][i[1]] = i[2:]

    for i in empty_cells_in_order:
        #if an usolved cell has only one possible value, replace the value of the cell in the grid with its only possible value
        if len(i) == 3:
            grid[i[0]][i[1]] = i[2]
            #compare the location of every unknown cell with one possible value with the location of every other unknown cell, to remove the value from their list of... 
            #...possible vlaues if in the same row, column, or square
            for j in empty_cells_in_order: #for each cell listed in empty grid list 
                #if the cells being compared are not the same cell
                if i != j:
                    #if the cell has more than one possible value 
                    if len(j)>3:
                        #if cell j has the same row index as cell i 
                        if j[0] == i[0]:
                            for poss_val in grid[j[0]][j[1]]:
                                #remove cell i's new value from the list of possible values for cell j (in the same row), if present
                                if poss_val == i[2]:
                                    remove_same_poss(grid[j[0]][j[1]], i[2])
                        #if cell j has the same column index as cell i 
                        if j[1] == i[1]: 
                            for poss_val in grid[j[0]][j[1]]:
                                #remove cell i's new value from the list of possible values for cell j (in the same column), if present 
                                if poss_val == i[2]:
                                    remove_same_poss(grid[j[0]][j[1]], i[2])

                        #if cell j is in the same square as cell i
                        square_int_i = same_square_check(i[0], i[1], n_rows, n_cols)
                        square_int_j = same_square_check(j[0], j[1], n_rows, n_cols)
                        if square_int_i == square_int_j:
                            for poss_val in grid[j[0]][j[1]]:
                                #remove cell i's new value from the list of possible values for cell j (in the same sqaure), if present 
                                if poss_val == i[2]:
                                    remove_same_poss(grid[j[0]][j[1]], i[2])
    #print ('grid1', np.array(grid))  

    #if there are any more lists in the grid, replace them with '0' -> so that the function can be called again
    for row in range(0, n_rows*n_cols):
        for col in range(0, n_rows*n_cols):
            if isinstance(grid[row][col], list):
                grid[row][col] = 0

    #if there are still unsolved cells in the grid, check if there are any cells with only one possible value
    empty_cells_in_order_2 = min(grid, n_rows, n_cols) #the (row, col, possible_vals) for each empty space, in order of number of possibilities after each iteration of function 
    #if there are no more unsolved cells in the grid
    if len(empty_cells_in_order_2) == 0:
        wavefront(grid, n_rows, n_cols) #call wavefront to run check_solution on the grid 
    #if there are unsolved cells in the grid 
    if len(empty_cells_in_order_2) > 0:
        #if there are unsolved cells with only one possible value 
        if len(empty_cells_in_order_2[0]) == 3: 
            wavefront(grid, n_rows, n_cols) #call wavefront to keep the 
        #if there are only unknown cells with more than one possible value
        if len(empty_cells_in_order_2[0]) >3: 
            #set the value of the cell with the least possible values as a randomly chosen possible value, and then call wavefront again 
            first_rand_cell = empty_cells_in_order_2[0] 
            grid[first_rand_cell[0]][first_rand_cell[1]] = random.choice(first_rand_cell[2:])
            wavefront(grid, n_rows, n_cols)

#wavefront(grid1, 2, 2)
#wavefront(grid2, 2, 2)
#wavefront(grid3, 2, 2)
#wavefront(grid4, 2, 2)
#wavefront(grid5, 2, 2)
wavefront(grid6, 2, 3)

