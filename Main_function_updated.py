#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:25:45 2023

@author: finlaymichael
"""

def recursive_solver(grid):
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
        return None #backtrack
    
    
    for i in possible_options:
        #place each possible value into the grid
        grid[n_rows][n_cols] = i
        
        #attempt to solve the sudoku
        result = recursive_solver(grid, explain)
        #if the sudoku is solved, return the solved grid
        if result is not None:
            return result
        
        #If we couldn't find a solution, the value must be wrong
        #Reset the grid for the next iteration of the loop
        grid[n_rows][n_cols] = 0  
        
    return None  # Unable to solve the puzzle