# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:51:02 2023

@author: charl
"""


def main():
    
    position_2x2 = 0
    position_3x2 = 0
    position_3x3 = 0
    
    input_2x2 = []
    input_3x2 = []
    input_3x3 = []
    
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        explain = False
        
        if len(sys.argv) > 1 and sys.argv[1] == '-explain':
            explain = True
            
        if len(sys.argv) > 1 and sys.argv[1] == "-hint":
            empties = empty_cell_list(grid)
            solution = recursive_solver(grid, explain)
            hint_solution = hint(empties, grid)
            if hint_solution is not None:
                for i in hint_solution:
                    print(i)
                    
        if len(sys.argv) > 1 and sys.argv[1] == '-profile':
            
            time_vals = []
            difficulty = len(empty_cell_list(grid))
            for timed in range(0,2):
                start_time = time.time()
                recursive_solver(grid, explain)
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
                
        else:
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
    
    
def hint(empty_list, board):
    hint_num = int(sys.argv[2])
    random_list = random.sample(range(0,len(empty_list)-1),(len(empty_list)-hint_num))
    for i in range(len(random_list)):
        empty_list.pop(random_list[i])
    for j in range(len(empty_list)):
        board[empty_list[i][0]][empty_list[i][1]] = 0
    return board 