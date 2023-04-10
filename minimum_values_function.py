# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:28:15 2023

@author: charl
"""

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
    #iterates across the passed board and returns the position vector of any empty spaces
    
    position = 0
    empties = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                empties.append([]) #adds an empty slot to the nested list
                empties[position].extend([row, col])#fills that empty slot with a coord
                position = position + 1
    
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
    #each empty slot can hold then returns the slot with the least possible values 
    
    
    min_remaining_values = len(board) + 1 #sets the maximum values possible 
    min_row, min_col = None, None #if min_row and min_col stay as none then the grid is complete
    empties = empty_cell_list(board)
    for i in range(len(empties)):
        remaining_values = len(find_possible_values(board, empties[i][0], empties[i][1]))
        if remaining_values < min_remaining_values:
            remaining_values = min_remaining_values
            min_row, min_col = empties[i][0], empties[i][1]
    
    
    return min_row, min_col