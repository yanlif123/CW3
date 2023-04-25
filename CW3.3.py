#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:09:39 2023

@author: finlaymichael
"""

import sys
import random
import copy
import time
import math
#Grids 1-4 are 2x2
puzzle = [
    [0, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 6, 0, 4, 0, 0, 0, 0],
    [5, 8, 0, 0, 9, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 3, 0, 0, 4],
    [4, 1, 0, 0, 8, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 5],
    [2, 0, 0, 0, 1, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 8, 0, 5, 7],
]

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



grids = [(puzzle, 3, 3), (grid6, 2, 3)]

def recursive_solver(grid, explain=False):
    """
    Solves a Sudoku puzzle using recursive backtracking starting with the empty cell with the least possible options
    """
    #Finding the empty cell with the fewest possible values
    n_rows, n_cols = find_min_remaining_values(grid)
    
    #If there are no empty cells, the puzzle is solved
    if n_rows is None:
        return grid
    
    possible_options = find_possible_options(grid, n_rows, n_cols) #working out the possible values for the cell with the minimum possible values in the grid
    
    if not possible_options:
        return None
    
    
    for i in possible_options:
        #place each possible value into the grid
        grid[n_rows][n_cols] = i
        if explain is True:
            print("Put", i,"in location (",n_rows+1,",", n_cols+1,")") 
        #attempt to solve the sudoku
        result = recursive_solver(grid, explain)
        #if the sudoku is solved, return the solved grid
        if result is not None:
            return result
        
        #If we couldn't find a solution, that must mean this value is incorrect.
        #Reset the grid for the next iteration of the loop
        grid[n_rows][n_cols] = 0  
        if explain is True:
            print("for (", n_rows, n_cols, "),", i,"doesn't work, so we backtrack")
    
    return None  # Unable to solve the puzzle


def find_possible_options(grid, n_rows, n_cols):
    
    #first create a list of all the possible values for the nxn grid
    possible_values = [i for i in range(1, len(grid[n_rows]) + 1)]
    
    for i in range(len(grid[n_rows])):
        if grid[n_rows][i] in possible_values:
            possible_values.remove(grid[n_rows][i])

    for i in range(len(grid[n_rows])):
        if grid[i][n_cols] in possible_values:
            possible_values.remove(grid[i][n_cols])
            
    box_value = int(len(grid) ** 0.5)
    first_row = (n_rows // box_value) * box_value
    first_column = (n_cols // (len(grid[n_rows]) // box_value)) * (len(grid[n_rows]) // box_value)
    
    for i in range(first_row, first_row + box_value):
        for j in range(first_column, first_column + (len(grid[n_rows]) // box_value)):
            if grid[i][j] in possible_values:
                possible_values.remove(grid[i][j])
    
    return list(possible_values)
                       


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
        remaining_values = len(find_possible_options(board, empties[i][0], empties[i][1]))
        if remaining_values < min_remaining_values:
            remaining_values = min_remaining_values
            min_row, min_col = empties[i][0], empties[i][1]
    
    
    return min_row, min_col


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


def check_solution(board, n_rows, n_cols):
	'''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
	n = n_rows*n_cols

	for row in board:
		if check_section(row, n) == False:
			return False

	for i in range(n_rows**2):
		column = []
		for row in board:
			column.append(row[i])

		if check_section(column, n) == False:
			return False

	squares = get_squares(board, n_rows, n_cols)
	for square in squares:
		if check_section(square, n) == False:
			return False

	return True


def main():
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        explain = False
        if len(sys.argv) > 1 and sys.argv[1] == '-explain':
            explain = True
        solution = recursive_solver(grid, explain)
        if solution is not None:
            for i in solution:
                print(i)
        else:
            print("Solution is unsolvable")
        if check_solution(solution, n_rows, n_cols):
            print("grid is correct")
        else:
            print("grid is incorrect")
        
   
    
   
if __name__ == "__main__":
    main()
























