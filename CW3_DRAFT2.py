import random
import copy
import time
import matplotlib.pyplot as plt
import sys
import numpy as np

''''''''''''''''''''''''''''''''''
DO NOT CHANGE CODE ABOVE THIS LINE
'''''''''''''''''''''''''''''''''

grid1 = [
		[1, 0, 0, 2],
		[0, 0, 1, 0],
		[0, 1, 0, 4],
		[0, 0, 0, 1]]



grid2 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]



grid3 = [
		[5, 3, 0, 0, 7, 0, 0, 0, 0],
		[6, 0, 0, 1, 9, 5, 0, 0, 0],
		[0, 9, 0, 0, 0, 0, 0, 6, 0],
		[8, 0, 0, 0, 6, 0, 0, 0, 3],
		[4, 0, 0, 8, 0, 3, 0, 0, 1],
		[7, 0, 0, 0, 2, 0, 0, 0, 0],
		[0, 6, 0, 0, 0, 0, 2, 8, 0],
		[0, 0, 0, 4, 1, 9, 0, 0, 5],
		[0, 0, 0, 0, 8, 0, 0, 7, 0]]

grid4 = [
		[0, 0, 4, 0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0, 3, 0, 0],
		[1, 0, 0, 0, 4, 2, 5, 0, 7],
		[0, 5, 0, 0, 0, 1, 0, 0, 0],
		[0, 0, 6, 0, 5, 0, 0, 9, 0],
		[0, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 0, 3, 0, 0, 0, 4],
		[0, 0, 7, 0, 0, 0, 0, 3, 0],
		[3, 0, 0, 2, 0, 0, 1, 0, 0]]


grids = [(grid1, 2, 2), (grid2, 2, 3), (grid3, 3, 3), (grid4,3,3)]

''''''''''
Functions:
'''''''''''

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
			elif type(grid[i][j]) == list:
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
			if board[row][col] == 0 or type(board[row][col]) ==  list:
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
	viable = [x for x in range(1,len(grid)+1) if x not in neighbours]
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

def list_solve(grid, n_rows, n_cols):
	'''
	Inputs: grid with number of rows and columns.

			(possible issue here in that the question asks for
	 		the input to be grids such as those in 'gridsl' list
	 		above but the function also works for the same grids that
			the recursive solve function does. It does this because I
			have modified the find_empty() and empty_cell_list() to
			also treat list type elements in the grids as empty spaces.

	Outputs: Solved grid.
	'''

	# if no empty slots are present check solution of the grid.
	minn = min(grid, n_rows, n_cols)
	empty = find_empty(grid)
	if not empty:
		if check_solution(grid, n_rows, n_cols):
			return grid
		else:
			return 'None'
	if len(minn) > 0:
		if len(minn) < 40:

			for lst in minn:
				#reducing size of each space (list) in grid by using poss function.
				# (only eliminating values which have already been placed in the grid)
				grid[lst[0]][lst[1]] = poss(grid, n_rows, n_cols, lst[0], lst[1])



			# If there exists a list containing only one possible value:
			# replace the list with the value itself and use new grid for recursion.
			if len(minn[0]) == 3:
				grid[minn[0][0]][minn[0][1]] = grid[minn[0][0]][minn[0][1]][0]
				return list_solve(grid, n_rows, n_cols)

			# If no empty slots with a single possible value exist:
			# for each possible value for the space with lowest possible values, create
			# a grid for each possible value where one is chosen and recursively solve.
			elif len(minn[0]) > 3:
				for index in range(2, len(minn[0])):
					option = minn[0][index]
					grid[minn[0][0]][minn[0][1]] = option
					return list_solve(grid, n_rows, n_cols)


	# The following code is using the x-wing method to eliminate candidate values.
	# It is a more obscure and painstaking method of finding solutions for empty
	#spaces and is therefore only used for difficult grids.
		elif len(minn) >= 40:
			for lst in minn:
				#reducing size of each space (list) in grid by using poss function.
				# (only eliminating values which have already been placed in the grid)
				grid[lst[0]][lst[1]] = poss(grid, n_rows, n_cols, lst[0], lst[1])
			#if any spaces with 1 possible value replacing that space with 1 possible value.
			for row in grid:
				for col in range(len(grid)):
					if type(row[col]) == list:
						if len(row[col]) == 1:
							row[col] = row[col][0]
			#checking whether there are two spaces in a row which share a candidate value:
			for space1 in minn:
				for space2 in minn:
					if space1[0] == space2[0] and space1 != space2:
						#defining the row
						r1 = space1[0]
						for index1 in range(2, len(space1)):
							for index2 in range(2, len(space2)):
								if space1[index1] == space2[index2]:
									#defining the columns containing the spaces
									col1 = space1[1]
									col2 = space2[1]
									number = space1[index1]

									# making sure there are no other spaces in the row with the same candidate value:

									third_r1 = filter(lambda x: type(x) == list and grid[r1].index(x) != col1 and grid[r1].index(x) != col2, grid[r1])
									candidates_r1 = [x for x in lst[2:] for lst in third_r1]

									if all(values != number for values in candidates_r1):

										#constructing list of other spaces in the grid:

										others = filter(lambda x: x != r1, minn)
										#checking whether there is the same formation of
										# possible values in another row (this could make an x wing):
										for space3 in others:
											for space4 in others:
												if space3[0] == space4[0] and space3 != space4:
													if space3[1] == col1 or space4[1] == col1:
														if space3[1] == col2 or space4[1] == col2:
															r2 = space3[0]
															for index3 in range(2, len(space3)):
																for index4 in range(2, len(space4)):
																	if space3[index3] == number and space4[index4] == number:
																		# making sure there are no other spaces in row 2 with the same candidate value:

																		third_r2 = filter(lambda x: type(x) == list and grid[r2].index(x) != col1 and grid[r2].index(x) != col2, grid[r2])
																		candidates_r2 = [x for x in lst[2:] for lst in third_r2]

																		if all(values != number for values in candidates_r2):

																			# if this point is reached the criteria for an x-wing is satisfied.
																			# removing the value in question from all cells in either column not
																			# in either row of the x-wing.
																			action_rows = [x for x in range(0,len(grid)) if x != r1 or r2]
																			for row in action_rows:
																				if type(grid[row][col1]) == list:
																					grid[row][col1] = [x for x in grid[row][col1] if x != number]
																				if type(grid[row][col2]) == list:
																					grid[row][col2] = [x for x in grid[row][col2] if x != number]






		# If there exists a list containing only one possible value:
		# replace the list with the value itself and use new grid for recursion.
		minn2 = min(grid, n_rows, n_cols)
		for lst in minn2:
			# reducing size of each space (list) in grid by using poss function.
			# (only eliminating values which have already been placed in the grid)
			grid[lst[0]][lst[1]] = poss(grid, n_rows, n_cols, lst[0], lst[1])
		#just making sure...:
		minn3 = min(grid, n_rows, n_cols)
		if len(minn3[0]) == 3:
			if type(grid[minn3[0][0]][minn3[0][1]]) == list:
				grid[minn3[0][0]][minn3[0][1]] = grid[minn3[0][0]][minn3[0][1]][0]
				#recursively solving once another value is added to the grid.
				return list_solve(grid, n_rows, n_cols)

		# If no empty slots with a single possible value exist:
		# for each possible value for the space with lowest possible values, create
		# a grid for each possible value where one is chosen and recursively solve.
		elif len(minn3[0]) > 3:
			for index in range(2, len(minn3[0])):
				option = minn3[0][index]
				grid[minn3[0][0]][minn3[0][1]] = option
				return list_solve(grid, n_rows, n_cols)


def recursive_solve(grid, n_rows, n_cols):
	'''
	This function uses recursion to exhaustively search all possible solutions to a grid
	until the solution is found

	args: grid, n_rows, n_cols
	return: A solved grid (as a nested list), or None
	'''
	#N is the maximum integer considered in this board
	n = n_rows*n_cols
	#Find an empty place in the grid
	empty = find_empty(grid)
	zipz = min(grid,n_rows,n_cols)
	empty_list = empty_cell_list(grid)
	#If there's no empty places left, check if we've found a solution
	if not empty:
		#If the solution is correct, return it.
		if check_solution(grid, n_rows, n_cols):
			return grid
		else:
			#If the solution is incorrect, return None
			return None
	else:
		# Defining the first priority empty cell in the list returned
		# by min() as row, col
		row, col = zipz[0][0], zipz[0][1]

	#Loop through possible values
	# translation: 'for i in the possible values for the first priority empty cell'
	for i in zipz[0][2:len(zipz[0])]:
			#Place the value into the grid
			grid[row][col] = i
				# Used the print statement above to attempt to debug, from the fact that it is not printing the
				# possible values for the last empty space in the grid it seems that it is failing to sub in the viable
				# value and this is causing the function to fail.
			#Recursively solve the grid
			ans = recursive_solve(grid, n_rows, n_cols)
			#If we've found a solution, return it
			if ans:
				return ans
			#If we couldn't find a solution, that must mean this value is incorrect.
			#Reset the grid for the next iteration of the loop
			grid[row][col] = 0 

	#If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
	return None




def explainer_v2(board, n_rows, n_cols, empty_list, explain):
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
	if explain == True:
		board_to_explain = board

	else:
		board_to_explain = recursive_solve(board,n_rows,n_cols)

		# If the board is unsolvable, return an error message
		if board is None:
			return "Error: Board is unsolvable."

	# Create a string to hold the explanation
	explanation = []

	# Iterate through each empty cell and fill it with a valid value
	for cell in empty_list:
		row, col = cell
		value = board_to_explain[row][col]
		# append the cell specific explanation to the overall explanation list
		explanation.append(f"Fill cell ({row}, {col}) with value {value}")

	return explanation

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


def same_square_check(row_ind, col_ind, n_rows, n_cols):
	"""
	Returns the indices of the square the cell is in - is used to check if two cells are in the same square
	Input:
    	cell's row index, cell's column index, grid row dimensions, grid column dimensions

	Return:
    	row index and column index of the square the cell is within
	"""
	col_sect = col_ind / n_cols  # if division is a float
	row_sect = row_ind / n_rows
	col_n = col_ind // n_cols  # if division is a wole number/ int
	row_n = row_ind // n_rows
	if type(col_sect) == float:
		col_interval = [col_n, col_n + 1]
	if type(col_sect) == int:
		col_interval = [col_sect - 1, col_sect]
	if type(row_sect) == float:
		row_interval = [row_n, row_n + 1]
	if type(row_sect) == int:
		row_interval = [row_sect - 1, row_sect]
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

	# check if the grid is solved, return grid if solved
	if check_solution(grid, n_rows, n_cols) == True:
		return grid

	# find the empty cells of the grid inputted
	empty_cells_in_order = min(grid, n_rows,
							   n_cols)  # returns the (row, col, possible_vals) for each empty space, in order of cell with least poss_vals

	# replace unsolved cells in grid (represented with a '0') with a list of possible values for that cell
	for i in empty_cells_in_order:
		grid[i[0]][i[1]] = i[2:]

	for i in empty_cells_in_order:
		# if an usolved cell has only one possible value, replace the value of the cell in the grid with its only possible value
		if len(i) == 3:
			grid[i[0]][i[1]] = i[2]
			# compare the location of every unknown cell with one possible value with the location of every other unknown cell, to remove the value from their list of...
			# ...possible vlaues if in the same row, column, or square
			for j in empty_cells_in_order:  # for each cell listed in empty grid list
				# if the cells being compared are not the same cell
				if i != j:
					# if the cell has more than one possible value
					if len(j) > 3:
						# if cell j has the same row index as cell i
						if j[0] == i[0]:
							for poss_val in grid[j[0]][j[1]]:
								# remove cell i's new value from the list of possible values for cell j (in the same row), if present
								if poss_val == i[2]:
									remove_same_poss(grid[j[0]][j[1]], i[2])
						# if cell j has the same column index as cell i
						if j[1] == i[1]:
							for poss_val in grid[j[0]][j[1]]:
								# remove cell i's new value from the list of possible values for cell j (in the same column), if present
								if poss_val == i[2]:
									remove_same_poss(grid[j[0]][j[1]], i[2])

						# if cell j is in the same square as cell i
						square_int_i = same_square_check(i[0], i[1], n_rows, n_cols)
						square_int_j = same_square_check(j[0], j[1], n_rows, n_cols)
						if square_int_i == square_int_j:
							for poss_val in grid[j[0]][j[1]]:
								# remove cell i's new value from the list of possible values for cell j (in the same sqaure), if present
								if poss_val == i[2]:
									remove_same_poss(grid[j[0]][j[1]], i[2])
	# print ('grid1', np.array(grid))

	# if there are any more lists in the grid, replace them with '0' -> so that the function can be called again
	for row in range(0, n_rows * n_cols):
		for col in range(0, n_rows * n_cols):
			if isinstance(grid[row][col], list):
				grid[row][col] = 0

	# if there are still unsolved cells in the grid, check if there are any cells with only one possible value
	empty_cells_in_order_2 = min(grid, n_rows,
								 n_cols)  # the (row, col, possible_vals) for each empty space, in order of number of possibilities after each iteration of function
	# if there are no more unsolved cells in the grid
	if len(empty_cells_in_order_2) == 0:
		return wavefront(grid, n_rows, n_cols)  # call wavefront to run check_solution on the grid
	# if there are unsolved cells in the grid
	if len(empty_cells_in_order_2) > 0:
		# if there are unsolved cells with only one possible value
		if len(empty_cells_in_order_2[0]) == 3:
			return wavefront(grid, n_rows, n_cols)  # call wavefront to keep the
		# if there are only unknown cells with more than one possible value
		if len(empty_cells_in_order_2[0]) > 3:
			recursive_solve(grid, n_rows, n_cols)
			return wavefront(grid, n_rows, n_cols)


def hint(empty_list, board, n_rows, n_cols, explain, file):
	'''
    Returns the sudoku board solved up to however many cells is specified in the command line
    args: empty_list - a list of the vector values of every empty cell on the board
          board - suduko nested list
          explain - a booleon variable to state if the function explains the hints or not (True and False respectively)
          file - a booleon variable to state if the the function takes a file input aswell as explaining the hints
    returns: board - board with N number of spaces filled based on the variable hint_num
             explanation -explanation of where the hints go and what they are
    '''
	hint_num = int(sys.argv[2])  # pulls the number of hints down from the command line

	if hint_num >= len(
			empty_list):  # if the number of hints is greater than the number of spaces it will return the completed board
		if explain == True:
			for i in explainer_v2(board, n_rows, n_cols, empty_list, explain=True):
				print(i)
		if file == True:
			explanation = '\n'.join([''.join(map(str, i)) for i in explainer_v2(board, n_rows, n_cols, empty_list, explain=True)])
			return (board, explanation)
		return board

	list_a = np.arange(0, len(empty_list)).tolist()
	random_list = random.sample(list_a, hint_num)  # random list of numbers to create a random hint everytime

	explain_list = []  # list of the position vectors of the hints used to explain the returned board

	for hint in range(0, (len(random_list))):
		explain_list.append(empty_list[random_list[hint]])

	new_empty_list = []  # empty list with all position vectors other than the hinted spaces

	for i in range(0, (len(empty_list))):
		if i not in random_list:
			new_empty_list.append(empty_list[i])

	for j in range(0, len(new_empty_list)):
		board[new_empty_list[j][0]][new_empty_list[j][1]] = 0  # sets all but the hinted spaces to 0 (empty)

	if explain == True:
		for i in explainer_v2(board, n_rows, n_cols, explain_list, explain=True):
			print(i)

	if file == True:
		explanation = '\n'.join([''.join(map(str, i)) for i in explainer_v2(board, n_rows, n_cols, explain_list, explain=True)])
		return (board, explanation)

	return board

def graph(graph_vals, matrix):
	graph_vals.sort(key=lambda x: x[0])
	# print(graph_vals)

	plt.style.use('ggplot')

	difficulty_num = []
	time_val = []

	for element in range(0, len(graph_vals)):
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



def random_solve(grid, n_rows, n_cols, max_tries=50000):
	'''
	This function uses random trial and error to solve a Sudoku grid

	args: grid, n_rows, n_cols, max_tries
	return: A solved grid (as a nested list), or the original grid if no solution is found
	'''

	for i in range(max_tries):
		possible_solution = fill_board_randomly(grid, n_rows, n_cols)
		if check_solution(possible_solution, n_rows, n_cols):
			return possible_solution

	return grid

def fill_board_randomly(grid, n_rows, n_cols):
	'''
	This function will fill an unsolved Sudoku grid with random numbers

	args: grid, n_rows, n_cols
	return: A grid with all empty values filled in
	'''
	n = n_rows*n_cols
	#Make a copy of the original grid
	filled_grid = copy.deepcopy(grid)

	#Loop through the rows
	for i in range(len(grid)):
		#Loop through the columns
		for j in range(len(grid[0])):
			#If we find a zero, fill it in with a random integer
			if grid[i][j] == 0:
				filled_grid[i][j] = random.randint(1, n)

	return filled_grid 

def solve(grid, n_rows, n_cols):

	'''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''

	return recursive_solve(grid, n_rows, n_cols)
	# return list_solve(grid,n_rows,n_cols)
	# return wavefront(grid,n_rows,n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================

'''


def main():
	print('====================================')
	print('To change the solver being used go into the solve() function in the python script')
	print('One can toggle between recursive_solve() (task 1), list_solve() (task 3) and wavefront() (task 3)')
	print('====================================')
	print('Flag syntax:')
	print('hint + file: these flags must be called in the order displayed on the left.')
	print('E.g. "Script.py -hint 5 -file input.txt output.txt')
	print('hint + explain: these flags must be called in the order displayed on the left.')
	print('E.g. "Script.py -hint 5 -explain')
	print('explain + file: these flags must be called in the order displayed on the left.')
	print('E.g. "Script.py -explain -file input.txt output.txt')
	print('hint + explain + file: these flags must be called in the order displayed on the left.')
	print('E.g. "Script.py -hint 5 -explain -file input.txt output.txt')
	print('====================================')
	position_2x2 = 0
	position_2x3 = 0
	position_3x3 = 0

	input_2x2 = []
	input_2x3 = []
	input_3x3 = []

	points = 0
	print("Running test script for Soduku Solver")

	print("====================================")

	only_profile = False
	for arg in sys.argv[1:]:
		if arg == "-profile":  # if '-profile' is present in the command line, it is the only flag that will be parsed
			only_profile = True

	# parsing the code so that if the profile flag is present among others, it will be the only flag that is parsed
	if only_profile:
		for (i, (grid, n_rows, n_cols)) in enumerate(grids):
			print("Solving grid: %d" % (i + 1))

			start_time = time.time()
			time_vals = []
			difficulty = len(empty_cell_list(grid))
			for timed in range(0, 2):
				start_time = time.time()
				solve(grid,n_rows,n_cols)  # solving the grid
				elapsed_time = time.time() - start_time
				time_vals.append(elapsed_time)
				averaged_time = sum(time_vals) / len(time_vals)

			elapsed_time = time.time() - start_time

			if grids[i][1] * grids[i][2] == 4:
			# if n_rows == 2 and n_cols ==2:
				input_2x2.append([])  # adds an empty slot to the nested list
				input_2x2[position_2x2].extend([averaged_time, difficulty])  # fills that empty slot with the graph vals
				position_2x2 = position_2x2 + 1

			if grids[i][1] * grids[i][2] == 6:
			# if n_rows == 2 and n_cols == 3:
				input_2x3.append([])  # adds an empty slot to the nested list
				input_2x3[position_2x3].extend([averaged_time, difficulty])  # fills that empty slot with the graph vals
				position_2x3 = position_2x3 + 1

			if grids[i][1] * grids[i][2] == 9:
			# if n_rows == 3 and n_cols == 3:
				input_3x3.append([])  # adds an empty slot to the nested list
				input_3x3[position_3x3].extend([averaged_time, difficulty])  # fills that empty slot with the graph vals
				position_3x3 = position_3x3 + 1

			if i == (len(grids) - 1):
				graph(input_2x2, 4)
				graph(input_2x3, 6)
				graph(input_3x3, 9)



			solution = solve(grid,n_rows,n_cols)

			# working out the size of a box in the grid
			n_rows = int(len(solution) ** 0.5)
			n_cols = int(len(solution) // n_rows)

			if solution is not None:  # if the solution exists, then print the board
				for k in solution:
					print(k)
			else:
				print("Solution is unsolvable")
			if check_solution(solution, n_rows, n_cols):  # if the solution is coreect, then print the board
				print("grid is correct")
				print("Solved in: %f seconds" % elapsed_time)
				points = points + 10
			else:
				print("grid is incorrect")
			print("Test script complete, Total points: %d" % points)



	else:
		# parsing the code if there are no flags present
		if len(sys.argv) == 1:
			for (i, (grid, n_rows, n_cols)) in enumerate(grids):
				print("Solving grid: %d" % (i + 1))
				# print(grid)
				start_time = time.time()

				solution = solve(grid,n_rows,n_cols)
				elapsed_time = time.time() - start_time

				if solution is not None:
					for k in solution:
						print(k)
				else:
					print("Solution is unsolvable")
				if check_solution(solution, n_rows, n_cols):
					print("grid is correct")
					print("Solved in: %f seconds" % elapsed_time)
					points = points + 10

				else:
					print("grid is incorrect")
			print("Test script complete, Total points: %d" % points)

		# parsing the code if there is only the explain flag present
		if len(sys.argv) == 2 and sys.argv[1] == '-explain':
			for (i, (grid, n_rows, n_cols)) in enumerate(grids):
				print("Solving grid: %d" % (i + 1))
				# print(grid)
				for i in explainer_v2(grid, n_rows, n_cols, empty_cell_list(grid), explain=False):
				# for i in explainer_v2(grid, n_rows, n_cols, empty_cell_list_2(grid), explain=False):
					print(i)

				start_time = time.time()

				solution = solve(grid,n_rows,n_cols)

				elapsed_time = time.time() - start_time

				if solution is not None:

					for k in solution:
						print(k)


				else:
					print("Solution is unsolvable")
				if check_solution(solution, n_rows, n_cols):
					print("grid is correct")
					print("Solved in: %f seconds" % elapsed_time)
					points = points + 10
				else:
					print("grid is incorrect")
			print("Test script complete, Total points: %d" % points)


		#parsing code if there is only hint present
		if len(sys.argv) == 3 and sys.argv[1] == "-hint":
			for (i, (grid, n_rows, n_cols)) in enumerate(grids):
				print("Adding hints to grid: %d" % (i + 1))
				empties = empty_cell_list(grid)
				start_time = time.time()

				solution = solve(grid,n_rows,n_cols)

				hint_solution = hint(empties, grid, n_rows, n_cols, explain=False, file=False)
				elapsed_time = time.time() - start_time

				print("Grid with hints added:")
				if hint_solution is not None:
					for element in hint_solution:
						print(element)
					print("Completed in: %f seconds" % elapsed_time)
				else:
					print('Unable to add hints.')
			print('Test script completed')


		# parsing the code if there is only the file flag present
		if len(sys.argv) > 3 and sys.argv[1] == '-file':

			input_file = sys.argv[2]
			output_file = sys.argv[3]
			start_time = time.time()

			with open(input_file, 'r') as f:
				grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]



			# working out the nxm size of a box in the grid
			n_rows = int(len(grid) ** 0.5)
			n_cols = int(len(grid) // n_rows)
			solution = solve(grid,n_rows,n_cols)
			elapsed_time = time.time() - start_time
			print("Solved in: %f seconds" % elapsed_time)



			if solution is not None:
				with open(output_file, 'w') as f:

					for i in solution:
						f.write(",".join(str(cell) for cell in i) + "\n")
			# 	for i in solution:
			# 		print(i)
			else:
				print("Solution is unsolvable")
			if check_solution(solution, n_rows, n_cols):
				print("correct grid has been written to output file")
				points = points + 10
			else:
				solution = solve(grid, n_cols, n_rows)
				if check_solution(solution, n_rows, n_cols):
					print("correct grid has been written to output file")
					points = points + 10
				else:
					print("grid is incorrect")
			print("Test script complete, Total points: %d" % points)

		# parsing the code if both the hint and file flags are present, in that order
		if len(sys.argv) > 4 and sys.argv[1] == '-hint' and sys.argv[3] == '-file':
			input_file = sys.argv[4]
			output_file = sys.argv[5]
			start_time = time.time()

			with open(input_file, 'r') as f:
				grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]

			# working out the nxm size of a box in the grid
			n_rows = int(len(grid) ** 0.5)
			n_cols = int(len(grid) // n_rows)

			# print(grid)
			empties = empty_cell_list(grid)

			if check_solution(recursive_solve(grid,n_rows,n_cols), n_rows, n_cols):
				solution = solve(grid, n_rows, n_cols)
				var = (solution, n_rows, n_cols)
				hint_solution = hint(empties, grid, n_rows, n_cols, explain=False, file=False)
			elif check_solution(recursive_solve(grid,n_cols,n_rows), n_cols, n_rows):
				solution = solve(grid, n_cols, n_rows)
				var = (solution, n_cols, n_rows)
				hint_solution = hint(empties, grid, n_cols, n_rows, explain=False, file=False)




			elapsed_time = time.time() - start_time
			print("Solved in: %f seconds" % elapsed_time)

			with open(output_file, 'w') as f:

				f.write("Grid With Hints:" + "\n")
				for i in hint_solution:
					f.write(",".join(str(cell) for cell in i) + "\n")

			if hint_solution is not None:
				# for i in solution:
				# 	print(i)
				with open(output_file, 'w') as f:

					f.write("Grid With Hints:" + "\n")
					for i in hint_solution:
						f.write(",".join(str(cell) for cell in i) + "\n")


			else:
				print("Solution is unsolvable")
				with open(output_file, 'w') as f:

					f.write("grid is unsolvable" + "\n")

			if check_solution(var[0],var[1],var[2]):
				print("Full solved grid has been written, if this is unwanted reduce number of hints")
				points = points + 10

			else:
				print("Grid with hints has been written")
			print("Test script complete")
		# parsing the code if the hint and explain flag are present, in that order

		if len(sys.argv) > 2 and len(sys.argv) == 4 and sys.argv[1] == '-hint' and sys.argv[3] == '-explain':
			for (i, (grid, n_rows, n_cols)) in enumerate(grids):
				print("Adding hints to grid: %d" % (i + 1))
				print(grid)
				start_time = time.time()
				empties = empty_cell_list(grid)
				solution = solve(grid,n_rows,n_cols)
				hint_solution = hint(empties, grid, n_rows, n_cols, explain=True, file=False)
				print("Grid with hints added:")
				if hint_solution is not None:
					for element in hint_solution:
						print(element)

				elapsed_time = time.time() - start_time
				print("Solved in: %f seconds" % elapsed_time)
				print("=========================")

		# parsing the code if both the explain and file flags are present - enter them in the command line in this order
		if len(sys.argv) > 2 and sys.argv[1] == '-explain' and sys.argv[2] == '-file':
			start_time = time.time()




			input_file = sys.argv[3]
			output_file = sys.argv[4]

			with open(input_file, 'r') as f:
				grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]

			# working out the nxm size of a box in the grid
			n_rows = int(len(grid) ** 0.5)
			n_cols = int(len(grid) // n_rows)

			explanation = '\n'.join([''.join(map(str, i)) for i in explainer_v2(grid, n_rows, n_cols, empty_cell_list(grid), explain=False)])


			if check_solution(recursive_solve(grid,n_rows,n_cols), n_rows, n_cols):
				solution = solve(grid, n_rows, n_cols)
			elif check_solution(recursive_solve(grid,n_cols,n_rows), n_cols, n_rows):
				solution = solve(grid, n_cols, n_rows)


			elapsed_time = time.time() - start_time
			print("Solved in: %f seconds" % elapsed_time)
			with open(output_file, 'w') as f:
				f.write(explanation)

				f.write("\n")

				for i in solution:
					f.write(",".join(str(cell) for cell in i) + "\n")

			if solution is not None:
				pass
			else:
				print("Solution is unsolvable")
			if check_solution(solution, n_rows, n_cols):
				print("Solved grid with explanation has been written to output file.")
				points = points + 10

			else:
				print("Obtained solution is incorrect, still written to output file.")
			print("Test script complete, Total points: %d" % points)


		# parsing code for -hint -explain -file int that order:.
		if len(sys.argv) > 5 and sys.argv[1] == '-hint' and sys.argv[3] == '-explain' and sys.argv[4] == '-file':

			start_time = time.time()

			input_file = sys.argv[5]
			output_file = sys.argv[6]

			with open(input_file, 'r') as f:
				grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]


			# working out the nxm size of a box in the grid
			n_rows = int(len(grid) ** 0.5)
			n_cols = int(len(grid) // n_rows)
			empties = empty_cell_list(grid)
			if check_solution(recursive_solve(grid,n_rows,n_cols), n_rows, n_cols):
				solution = solve(grid, n_rows, n_cols)
				var = (solution, n_rows, n_cols)
				hint_solution = hint(empties, grid, n_rows, n_cols, explain=False, file=True)
			elif check_solution(recursive_solve(grid,n_cols,n_rows), n_cols, n_rows):
				solution = solve(grid, n_cols, n_rows)
				var = (solution, n_cols, n_rows)
				hint_solution = hint(empties, grid, n_cols, n_rows, explain=False, file=True)

			with open(output_file, 'w') as f:

				f.write('\n')
				f.write(hint_solution[1])
				f.write("\n Grid with hints added: \n" )


				for i in hint_solution[0]:
					f.write(",".join(str(cell) for cell in i) + "\n")
			print('Grid with hints and explanation written to output file')




if __name__ == "__main__":
	main()
