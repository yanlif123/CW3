#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:16:54 2023

@author: finlaymichael
"""

def find_viable_values(grid, n_rows, n_cols):
    viable_values = set(range(1, len(grid[n_rows]) + 1))
    
    # Check the row and column
    for i in range(len(grid[n_rows])):
        if grid[n_rows][i] in viable_values:
            viable_values.remove(grid[n_rows][i])
    for i in range(len(grid)):
        if grid[i][n_cols] in viable_values:
            viable_values.remove(grid[i][n_cols])
    
    # Check the box
    box_size = int(len(grid) ** 0.5) #works out the number of rows of the grid
    box_row = (n_rows // box_size) * box_size #works out the row of the top left cell in the box that the inputted location row,col is a part of
    box_col = (n_cols // (len(grid[n_rows]) // box_size)) * (len(grid[n_rows]) // box_size) #works out the column of the top left cell in the box of the inputted cell location
    # these variables take into account that rows and columns are both zero-indexed - i.e. that (row = 3, col = 4) corresponds to the 4th row and 5th column
    for i in range(box_row, box_row + box_size): #ranges over the rows of the grid that the box is in
        for j in range(box_col, box_col + (len(grid[n_rows]) // box_size)): #ranges over the columns of the grid that the box is in
            if grid[i][j] in viable_values:
                viable_values.remove(grid[i][j])
    
    return list(viable_values)