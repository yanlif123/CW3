# -*- coding: utf-8 -*-
"""
Created on Wed May  3 14:38:18 2023

@author: charl
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import random
import copy
import time
import math
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




def recursive_solver(grid):
    """
    Solves a Sudoku puzzle using recursive backtracking starting with the empty cell with the least possible options
    """
    #Finding the empty cell with the fewest possible values
    copy = grid
    n_rows, n_cols = find_min_remaining_values(copy)

    #If there are no empty cells, the puzzle is solved
    if n_rows is None:
        return copy

    possible_options = find_possible_options(copy, n_rows, n_cols) #working out the possible values for the cell with the minimum possible values in the grid

    if not possible_options:
        return None


    for i in possible_options:
        #place each possible value into the grid
        copy[n_rows][n_cols] = i
        #if the explain flag exists in the command line, append the action of the solver into the 'explanation' string


        #attempt to solve the sudoku
        result = recursive_solver(copy)

        #adding the explanation for this specific cell position and number into the overall 'explanation' string

        #if the sudoku is solved, return the solved grid
        if result is not None:
            return result

        #If we couldn't find a solution, that must mean this value is incorrect.
        #Reset the grid for the next iteration of the loop
        copy[n_rows][n_cols] = 0  
        #if explain is True:
            #print("for (", n_rows, n_cols, "),", i,"doesn't work, so we backtrack")

    return None  # Unable to solve the puzzle


def find_possible_options(grid, n_rows, n_cols):
    """
    Returns a list of possible values for a certain nxm cell position on the sudoku board
    """
    #first create a list of all the possible values for the nxn grid
    possible_values = [i for i in range(1, len(grid[n_rows]) + 1)]

    #working out the values in the row already used
    for i in range(len(grid[n_rows])):
        if grid[n_rows][i] in possible_values:
            possible_values.remove(grid[n_rows][i])

    #working out the values in the column already used
    for i in range(len(grid[n_rows])):
        if grid[i][n_cols] in possible_values:
            possible_values.remove(grid[i][n_cols])


    box_value = int(len(grid) ** 0.5)

    #working out the position of the top left cell of the box that the grid position is in
    first_row = (n_rows // box_value) * box_value
    first_column = (n_cols // (len(grid[n_rows]) // box_value)) * (len(grid[n_rows]) // box_value)

    #working out the values in the box that have already been used
    for i in range(first_row, first_row + box_value):
        for j in range(first_column, first_column + (len(grid[n_rows]) // box_value)):
            if grid[i][j] in possible_values:
                possible_values.remove(grid[i][j])


    return list(possible_values)


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




#def empty_cell_list(board):
#    '''

#    Parameters
#    ----------
#    board : TYPE           nested list
      #      DESCRIPTION.   unfinished suduko grid displayed as a nested list
##    Returns
#    -------
 #   empties : TYPE         nested list
 #       DESCRIPTION        list of coordinates for the empty spaces in board
#    '''
#    #iterates across the passed board and returns the position vector of any empty spaces

#    position = 0
#    empties = []
#    for row in range(len(board)):
#        for col in range(len(board[row])):
 #           if board[row][col] == 0:
 #               empties.append([]) #adds an empty slot to the nested list
 #               empties[position].extend([row, col])#fills that empty slot with a coord
 #               position = position + 1

 #   return empties           

def empty_cell_list(board):
    """
    Returns a list of coordinates for the empty cells in a Sudoku board.
    """
    empties = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                empties.append((row, col))
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



#def check_sol(grid):



def graph(graph_vals, matrix):
    graph_vals.sort(key=lambda x: x[0])
    #print(graph_vals)

    plt.style.use('ggplot')

    difficulty_num = []
    time_val = []

    for element in range(0,len(graph_vals)):
        time_val.append(graph_vals[element][0])
        difficulty_num.append(graph_vals[element][1])

    x_pos = [i for i, _ in enumerate(difficulty_num)]

    plt.bar(x_pos, time_val, color='blue', width=0.1)
    if matrix == 4:
        plt.xlabel("2x2 Matrix")
    if matrix == 6:
        plt.xlabel("3x2 Matrix")
    if matrix == 9:
        plt.xlabel("3x3 Matrix")
    plt.ylabel("Averaged Time")
    plt.title("Suduko solver performance indicator")

    plt.xticks(x_pos, difficulty_num)

    plt.show()


def hint(empty_list, board, explain):
    hint_num = int(sys.argv[2])
    if hint_num >= len(empty_list):
        if explain == True:
            for i in explainer_v2(board, empty_list, explain = True):
                print(i)
        return board
    list_a = np.arange(0, len(empty_list)).tolist()
    random_list = random.sample(list_a, hint_num)
    #print(random_list, "random list")
    #print(empty_list, "empty list")
    explain_list = []
    
    for hint in range(0,(len(random_list))):
        explain_list.append(empty_list[random_list[hint]])
    #print(explain_list, "explain list")
    
    '''
    for i in range(0, (len(random_list))):
        
        empty_list.pop(random_list[i])
    '''
    new_empty_list = []
    for i in range(0, (len(empty_list))):
        if i not in random_list:
            new_empty_list.append(empty_list[i])
        
            
    
        
    #print(empty_list, "empty list")
    
    for j in range(0, len(new_empty_list)):
        board[new_empty_list[j][0]][new_empty_list[j][1]] = 0
    
    if explain == True:
        
        for i in explainer_v2(board, explain_list, explain = True):
            print(i)
    
    return board 


def explainer(board, grid):
    empty_list = empty_cell_list_2(grid)
    print(empty_list)
    explanations = []

    for i in empty_list:
        row, col = i

        value = board[row][col]
        print(value)
        explanations.append(f"put {value} into ({row+1}, {col+1})")

    return explanations

def explainer_v2(board, empty_list, explain):
    '''
    Parameters
    ----------
    board : list
        The Sudoku board, represented as a 2D list.
    empty_list : list
        A list of the empty cells in the board.
    
    Returns
    -------
    explanation : str
        A string explaining the steps taken to solve the board.
    '''
    # Create a copy of the board so that the original board is not modified
    #board_copy = [row[:] for row in board]
    if explain == True:
        board_to_explain = board
    # Use the recursive_solver function to solve the board
    else:
        board_to_explain = recursive_solver(board)
        
        # If the board is unsolvable, return an error message
        if board is None:
            return "Error: Board is unsolvable."
    
    

    # Create a string to hold the explanation
    explanation = []

    # Iterate through each empty cell and fill it with a valid value
    for cell in empty_list:
        row, col = cell
        value = board_to_explain[row][col]
        #board[row][col] = value
        explanation.append(f"Fill cell ({row}, {col}) with value {value}")

    # Check that the solved board is valid
    return explanation

'''
def explainer_v2(board, empty_list):
    '''
'''
    Parameters
    ----------
    board : list
        The Sudoku board, represented as a 2D list.
    empty_list : list
        A list of the empty cells in the board.
    
    Returns
    -------
    explanation : str
        A string explaining the steps taken to solve the board.
'''
'''
    # Create a copy of the board so that the original board is not modified
    #board_copy = [row[:] for row in board]
    if explain == True:
        board_to_explain = board
    # Use the recursive_solver function to solve the board
    board_to_explain = recursive_solver(board)

    # If the board is unsolvable, return an error message
    if board is None:
        return "Error: Board is unsolvable."

    # Create a string to hold the explanation
    explanation = []

    # Iterate through each empty cell and fill it with a valid value
    for cell in empty_list:
        row, col = cell
        value = board_to_explain[row][col]
        #board[row][col] = value
        explanation.append(f"Fill cell ({row}, {col}) with value {value}")

    # Check that the solved board is valid
    return explanation
'''

def empty_cell_list_2(board):
    empties = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                empties.append([row, col])

    return empties



def main():

    position_2x2 = 0
    position_3x2 = 0
    position_3x3 = 0

    input_2x2 = []
    input_3x2 = []
    input_3x3 = []

    points = 0
    print("Running test script for coursework 1")

    print("====================================")


    only_profile = False
    for arg in sys.argv[1:]:
        if arg == "-profile":
            only_profile = True

    #parsing the code so that if the profile flag is present among others, it will be the only flag that is parsed
    if only_profile:
        for (i, (grid, n_rows, n_cols)) in enumerate(grids):

            start_time = time.time()
            time_vals = []
            difficulty = len(empty_cell_list(grid))
            for timed in range(0,2):
                start_time = time.time()
                recursive_solver(grid)
                elapsed_time = time.time() - start_time
                time_vals.append(elapsed_time)
                averaged_time = sum(time_vals) / len(time_vals)

            if grids[i][1]*grids[i][2] == 4:
                input_2x2.append([]) #adds an empty slot to the nested list
                input_2x2[position_2x2].extend([averaged_time, difficulty])#fills that empty slot with the graph vals
                position_2x2 = position_2x2 + 1

            if grids[i][1]*grids[i][2] == 6:
                input_3x2.append([]) #adds an empty slot to the nested list
                input_3x2[position_3x2].extend([averaged_time, difficulty])#fills that empty slot with the graph vals
                position_3x2 = position_3x2 + 1

            if grids[i][1]*grids[i][2] == 9:
                input_3x3.append([]) #adds an empty slot to the nested list
                input_3x3[position_3x3].extend([averaged_time, difficulty])#fills that empty slot with the graph vals
                position_3x3 = position_3x3 + 1

            if i == (len(grids) - 1):
                graph(input_2x2, 4)
                graph(input_3x2, 6)
                graph(input_3x3, 9)



            elapsed_time = time.time() - start_time

            solution = recursive_solver(grid)

            n_rows = int(len(solution) ** 0.5)
            n_cols = int(len(solution) // n_rows)

            if solution is not None:
                for i in solution:
                    print(i)
            else:
                print("Solution is unsolvable")
            if check_solution(solution, n_rows, n_cols):
                print("grid is correct")
                print("Solved in: %f seconds" % elapsed_time)
                points = points + 10
            else:
                print("grid is incorrect")
            print("Test script complete, Total points: %d" % points)



    else:   
        #parsing the code if there are no flags present
        if len(sys.argv) == 1:
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):
                print(grid)
                start_time = time.time()

                solution = recursive_solver(grid)
                elapsed_time = time.time() - start_time


                if solution is not None:
                    for i in solution:
                        print(i) 
                else:
                    print("Solution is unsolvable")
                if check_solution(solution, n_rows, n_cols):
                    print("grid is correct")
                    print("Solved in: %f seconds" % elapsed_time)
                    points = points + 10

                else:
                    print("grid is incorrect")
            print("Test script complete, Total points: %d" % points)      

    #parsing the code if there is only the explain flag present
        if len(sys.argv) == 2 and sys.argv[1] == '-explain':
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):
                print(grid)

                for i in explainer_v2(grid, empty_cell_list_2(grid), explain = False):
                    print(i)


                start_time = time.time()

                solution = recursive_solver(grid)


                elapsed_time = time.time() - start_time

                if solution is not None:

                    for i in solution:
                        print(i)


                else:
                    print("Solution is unsolvable")
                if check_solution(solution, n_rows, n_cols):
                    print("grid is correct")
                    print("Solved in: %f seconds" % elapsed_time)
                    points = points + 10
                else:
                    print("grid is incorrect")
            print("Test script complete, Total points: %d" % points)
        
        if len(sys.argv) == 3 and sys.argv[1] == "-hint":
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):
                empties = empty_cell_list(grid)
                solution = recursive_solver(grid)
                hint_solution = hint(empties, grid, explain = False)
                print("NEW GRID")
                if hint_solution is not None:
                    for element in hint_solution:
                        print(element)

    #parsing the code if there is only the file flag present
        if len(sys.argv) > 1 and sys.argv[1] == '-file':
            input_file = sys.argv[2]
            output_file = sys.argv[3]
            start_time = time.time()

            with open(input_file, 'r') as f:
                grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]

            print(grid)
            solution = recursive_solver(grid)

        #working out the nxm size of a box in the grid
            n_rows = int(len(solution) ** 0.5)
            n_cols = int(len(solution) // n_rows)

            elapsed_time = time.time() - start_time
            print("Solved in: %f seconds" % elapsed_time)

            with open(output_file, 'w') as f:

                for i in solution:
                    f.write(",".join(str(cell) for cell in i) + "\n")

            if solution is not None:
                for i in solution:
                    print(i)
            else:
                print("Solution is unsolvable")
            if check_solution(solution, n_rows, n_cols):
                print("grid is correct")
                points = points + 10
            else:
                print("grid is incorrect")
            print("Test script complete, Total points: %d" % points)

        if len(sys.argv) > 3 and sys.argv[1] == '-hint' and sys.argv[3] == '-explain':
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):
                empties = empty_cell_list(grid)
                solution = recursive_solver(grid)
                hint_solution = hint(empties, grid, explain = True)
                
                if hint_solution is not None:
                    for element in hint_solution:
                        print(element)
                print("=========================")
                print("NEW GRID")
                
                

    #parsing the code if both the explain and file flags are present - enter them in the command line in this order
        if len(sys.argv) > 2 and sys.argv[1] == '-explain' and sys.argv[2] == '-file':
        #if len(sys.argv) > 1 and sys.argv[2] == '-file':

                start_time = time.time()

                input_file = sys.argv[3]
                output_file = sys.argv[4]

                with open(input_file, 'r') as f:
                    grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]

                print(grid)

                explanation = '\n'.join([''.join(map(str, i)) for i in explainer_v2(grid, empty_cell_list_2(grid))])
                print(explanation)

                solution = recursive_solver(grid)



            #working out the nxm size of a box in the grid
                n_rows = int(len(solution) ** 0.5)
                n_cols = int(len(solution) // n_rows)

                elapsed_time = time.time() - start_time
                print("Solved in: %f seconds" % elapsed_time)
                with open(output_file, 'w') as f:
                    f.write(explanation)
                    #for i in explainer_v2(grid, empty_cell_list_2(grid)):
                        #f.write(' '.join(map(str, i)) + "\n")


                    for i in solution:
                        f.write(",".join(str(cell) for cell in i) + "\n")


                if solution is not None:
                    for i in solution:
                        print(i)
                else:
                    print("Solution is unsolvable")
                if check_solution(solution, n_rows, n_cols):
                    print("grid is correct")
                    points = points + 10
                else:
                    print("grid is incorrect")
                print("Test script complete, Total points: %d" % points)




if __name__ == "__main__":
    main()