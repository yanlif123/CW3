import random
import copy
import time
import matplotlib.pyplot as plt
import sys

#Grids 1-4 are 2x2
grid1 = [
                [1, 0, 4, 2],
                [4, 2, 1, 3],
                [2, 1, 3, 4],
                [3, 4, 2, 1]]

grid1l = [
                [1, [1,2,3,4], 4, 2],
                [4, 2, 1, 3],
                [2, 1, 3, 4],
                [3, 4, 2, 1]]

grid2 = [
                [1, 0, 4, 2],
                [4, 2, 1, 3],
                [2, 1, 0, 4],
                [3, 4, 2, 1]]

grid2l = [
                [1, [1,2,3,4], 4, 2],
                [4, 2, 1, 3],
                [2, 1, [1,2,3,4], 4],
                [3, 4, 2, 1]]

grid3 = [
                [1, 0, 4, 2],
                [4, 2, 1, 0],
                [2, 1, 0, 4],
                [0, 4, 2, 1]]

grid3l = [
                [1, [1,2,3,4], 4, 2],
                [4, 2, 1, [1,2,3,4]],
                [2, 1, [1,2,3,4], 4],
                [[1,2,3,4], 4, 2, 1]]

grid4 = [
                [1, 0, 4, 2],
                [0, 2, 1, 0],
                [2, 1, 0, 4],
                [0, 4, 2, 1]]

grid4l = [
                [1, [1,2,3,4], 4, 2],
                [[1,2,3,4], 2, 1, [1,2,3,4]],
                [2, 1, [1,2,3,4], 4],
                [[1,2,3,4], 4, 2, 1]]

grid5 = [
                [1, 0, 0, 2],
                [0, 0, 1, 0],
                [0, 1, 0, 4],
                [0, 0, 0, 1]]

grid5l = [
                [1, [1,2,3,4], [1,2,3,4], 2],
                [[1,2,3,4], [1,2,3,4], 1, [1,2,3,4]],
                [[1,2,3,4], 1, [1,2,3,4], 4],
                [[1,2,3,4], [1,2,3,4], [1,2,3,4], 1]]

grid6 = [
                [0, 0, 6, 0, 0, 3],
                [5, 0, 0, 0, 0, 0],
                [0, 1, 3, 4, 0, 0],
                [0, 0, 0, 0, 0, 6],
                [0, 0, 1, 0, 0, 0],
                [0, 5, 0, 0, 6, 4]]

grid6l = [
                [[1,2,3,4,5,6], [1,2,3,4,5,6], 6, [1,2,3,4,5,6], [1,2,3,4,5,6], 3],
                [5, [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]],
                [[1,2,3,4,5,6], 1, 3, 4, [1,2,3,4,5,6], [1,2,3,4,5,6]],
                [[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], 6],
                [[1,2,3,4,5,6], [1,2,3,4,5,6], 1, [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]],
                [[1,2,3,4,5,6], 5, [1,2,3,4,5,6], [1,2,3,4,5,6], 6, 4]]

grid7 = [
                [8, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 6, 0, 0, 0, 0, 0],
                [0, 7, 0, 0, 9, 0, 2, 0, 0],
                [0, 5, 0, 0, 0, 7, 0, 0, 0],
                [0, 0, 0, 0, 4, 5, 7, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 0, 1, 0, 0, 0, 0, 6, 8],
                [0, 0, 8, 5, 0, 0, 0, 1, 0],
                [0, 9, 0, 0, 0, 0, 4, 0, 0]]

grid8 = [
                [1, 0, 0, 0, 0, 7, 0, 9, 0],
                [0, 3, 0, 0, 2, 0, 0, 0, 8],
                [0, 0, 9, 6, 0, 0, 5, 0, 0],
                [0, 0, 5, 3, 0, 0, 9, 0, 0],
                [0, 1, 0, 0, 8, 0, 0, 0, 2],
                [6, 0, 0, 0, 0, 4, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 4, 0, 0, 0, 0, 0, 0, 7],
                [0, 0, 7, 0, 0, 0, 3, 0, 0]]

grid9 = [
                [0, 0, 4, 6, 0, 8, 9, 1, 2],
                [0, 7, 2, 0, 0, 0, 3, 4, 8],
                [1, 0, 0, 3, 4, 2, 5, 0, 7],
                [0, 5, 9, 7, 0, 1, 4, 2, 0],
                [0, 2, 6, 0, 5, 0, 7, 9, 0],
                [0, 1, 3, 9, 0, 4, 8, 5, 0],
                [9, 0, 1, 5, 3, 7, 0, 0, 4],
                [2, 8, 7, 0, 0, 0, 6, 3, 0],
                [3, 4, 5, 2, 0, 6, 1, 0, 0]]



grid11 = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 0]]

grid10 = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 0, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [0, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 0, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 0]]

grid81 =[
                [8, 6, 4, [2, 7], [1, 2, 7], [1, 2], 9, 5, 3],
                [9, 2, 3, 6, 5, 4, 8, 7, 1],
                [1, 7, 5, 8, 9, [3, 8], 2, 4, 6],
                [[3, 6], 5, 2, [8], [6, 8], 7, 1, 9, 4],
                [[6], [1], 9, 3, 4, 5, 7, 8, 2],
                [[4, 7], [4, 8], [7], 1, [2, 8], [2, 8, 9], 6, 3, 5],
                [[2, 3, 4, 7], [3, 4], 1, [2, 4, 7, 9], [2, 3, 7], [2, 3, 9], 5, 6, 8],
                [[2, 4, 7], [4], 8, 5, [2, 6, 7], [2, 6], 3, 1, 9],
                [[3, 5], 9, 6, [8], [1, 3, 8], [1, 3, 8], 4, 2, 7]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 2, 3)]
gridsl = [(grid1l, 2, 2), (grid2l, 2, 2), (grid3l, 2, 2), (grid4l, 2, 2), (grid5l, 2, 2), (grid6l, 2, 3)]
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
    copy = grid
    minn = min(grid, n_rows, n_cols)
    empty = find_empty(grid)
    if not empty:
        if check_solution(grid, n_rows, n_cols):
            return grid
        else:
            return None

    elif len(minn) > 0 and grid == copy:
        print(grid)
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



# print(list_solve(grid9,3,3))
print(len(min(grid10,3,3)))
print(list_solve(grid10,3,3))

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



def explainer_v2(board, empty_list, n_rows, n_cols):
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
    # board_copy = [row[:] for row in board]

    # Use the recursive_solver function to solve the board
    solved_board = recursive_solve(board, n_rows, n_cols)

    # If the board is unsolvable, return an error message
    if board is None:
        return "Error: Board is unsolvable."

    # Create a string to hold the explanation
    explanation = []

    # Iterate through each empty cell and fill it with a valid value
    for cell in empty_list:
        row, col = cell
        value = solved_board[row][col]
        board[row][col] = value
        explanation.append(f"Filled cell ({row+1}, {col+1}) with value {value}")

    # Check that the solved board is valid
    return explanation


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

    #return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)
    # return list_solve(grid,n_rows,n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():

    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i+1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i+1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i+1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)

#
if __name__ == "__main__":
    main()


def main():
    position_2x2 = 0
    position_3x2 = 0
    position_3x3 = 0

    input_2x2 = []
    input_3x2 = []
    input_3x3 = []

    points = 0
    print("Running test script for Soduku Solver")

    print("====================================")

    only_profile = False
    for arg in sys.argv[1:]:
        if arg == "-profile":
            only_profile = True

    # parsing the code so that if the profile flag is present among others, it will be the only flag that is parsed
    if only_profile:
        points = 0
        for (i, (grid, n_rows, n_cols)) in enumerate(grids):
            print("Solving grid: %d" % (int(i) + 1))
            start_time = time.time()
            time_vals = []
            difficulty = len(empty_cell_list(grid))

            for timed in range(0, 2):
                start_time = time.time()
                recursive_solve(grid,n_rows,n_cols)
                elapsed_time = time.time() - start_time
                time_vals.append(elapsed_time)
                averaged_time = sum(time_vals) / len(time_vals)

            if grids[i][1] * grids[i][2] == 4:
                input_2x2.append([])  # adds an empty slot to the nested list
                input_2x2[position_2x2].extend([averaged_time, difficulty])  # fills that empty slot with the graph vals
                position_2x2 = position_2x2 + 1

            if grids[i][1] * grids[i][2] == 6:
                input_3x2.append([])  # adds an empty slot to the nested list
                input_3x2[position_3x2].extend([averaged_time, difficulty])  # fills that empty slot with the graph vals
                position_3x2 = position_3x2 + 1

            if grids[i][1] * grids[i][2] == 9:
                input_3x3.append([])  # adds an empty slot to the nested list
                input_3x3[position_3x3].extend([averaged_time, difficulty])  # fills that empty slot with the graph vals
                position_3x3 = position_3x3 + 1

            if i == (len(grids) - 1):
                graph(input_2x2, 4)
                graph(input_3x2, 6)
                graph(input_3x3, 9)

            elapsed_time = time.time() - start_time

            solution = recursive_solve(grid,n_rows,n_cols)

            n_rows = int(len(solution) ** 0.5)
            n_cols = int(len(solution) // n_rows)

            if solution is not None:
                for k in solution:
                    print(k)
            else:
                print("Solution is unsolvable")
                print("====================================")
            if check_solution(solution, n_rows, n_cols):
                print("grid %d correct" % (i+1))
                print("Solved in: %f seconds" % elapsed_time)
                print("====================================")
                points = points + 10
            else:
                print("grid %d incorrect" % (i + 1))
                print("====================================")
        print("Test script complete, Total points: %d" % points)



    else:
        # parsing the code if there are no flags present
        points = 0
        if len(sys.argv) == 1:
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):

                start_time = time.time()

                solution = recursive_solve(grid,n_rows,n_cols)
                elapsed_time = time.time() - start_time
                print("Solving grid %d:" % (i + 1))
                if solution is not None:
                    for k in solution:
                        print(k)


                else:
                    print("Solution is unsolvable")
                    print("====================================")
                if check_solution(solution, n_rows, n_cols):
                    print("grid %d correct" % (i + 1))
                    print("Solved in: %f seconds" % elapsed_time)
                    points = points + 10
                    print("====================================")
                else:
                    print("grid %d incorrect" % (i + 1))
                    print("====================================")
            print("Test script complete, Total points: %d" % points)

        # parsing the code if there is only the explain flag present
        points = 0
        if len(sys.argv) == 2 and sys.argv[1] == '-explain':
            for (i, (grid, n_rows, n_cols)) in enumerate(grids):

                print(explainer_v2(grid, empty_cell_list(grid), n_rows, n_cols))

                start_time = time.time()

                solution = recursive_solve(grid, n_rows, n_cols)

                elapsed_time = time.time() - start_time


                if solution is not None:
                    for k in solution:
                        print(k)
                else:
                    print("Solution is unsolvable")

                if check_solution(solution, n_rows, n_cols):
                    print("grid %d correct" % (i + 1))
                    print("Solved in: %f seconds" % elapsed_time)
                    points = points + 10
                    print("====================================")
                else:
                    print("grid %d incorrect" % (i + 1))
                    print("====================================")

            print("Test script complete, Total points: %d" % points)

        # parsing the code if there is only the file flag present
        if len(sys.argv) > 1 and sys.argv[1] == '-file':
            input_file = sys.argv[2]
            output_file = sys.argv[3]
            start_time = time.time()

            with open(input_file, 'r') as f:
                grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]

            print(grid)
            n_rows = int(len(grid) ** 0.5)
            n_cols = int(len(grid) // n_rows)

            solution = recursive_solve(grid,n_rows,n_cols)


            # working out the nxm size of a box in the grid


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
                print("Solved in: %f seconds" % elapsed_time)
                points = points + 10
            else:
                print("grid is incorrect")
            print("Test script complete, Total points: %d" % points)

        # parsing the code if both the explain and file flags are present - enter them in the command line in this order
        if len(sys.argv) > 2 and sys.argv[1] == '-explain' and sys.argv[2] == '-file':
            # if len(sys.argv) > 1 and sys.argv[2] == '-file':

            start_time = time.time()

            input_file = sys.argv[3]
            output_file = sys.argv[4]

            with open(input_file, 'r') as f:
                grid = [[int(cell) for cell in line.strip().split(",")] for line in f.readlines()]

            print(grid)

            explanation = '\n'.join([''.join(map(str, i)) for i in explainer_v2(grid, empty_cell_list(grid),n_rows,n_cols)])
            print(explanation)

            solution = recursive_solve(grid,n_rows,n_cols)

            # working out the nxm size of a box in the grid
            n_rows = int(len(solution) ** 0.5)
            n_cols = int(len(solution) // n_rows)

            elapsed_time = time.time() - start_time
            print("Solved in: %f seconds" % elapsed_time)
            with open(output_file, 'w') as f:
                f.write(explanation)
                # for i in explainer_v2(grid, empty_cell_list_2(grid)):
                # f.write(' '.join(map(str, i)) + "\n")

                for i in solution:
                    f.write(",".join(str(cell) for cell in i) + "\n")

            if solution is not None:
                for i in solution:
                    print(i)
            else:
                print("Solution is unsolvable")
            if check_solution(solution, n_rows, n_cols):
                print("grid %d correct" % (i+1))
                print("Solved in: %f seconds" % elapsed_time)
                points = points + 10
            else:
                print("grid %d incorrect" % (i + 1))
            print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    main()
