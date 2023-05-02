# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:20:08 2023

@author: charl
"""



def hint(empty_list, board):
    hint_num = int(sys.argv[2])
    if hint_num >= len(empty_list):
        return board
    list_a = np.arange(0, len(empty_list)-1).tolist()
    random_list = random.sample(list_a, len(empty_list)-(len(empty_list)-hint_num))
    print(empty_list)
    print(random_list, "random list")
    for i in range(0,(len(random_list)-1)):
        empty_list.pop(random_list[i])
    print(empty_list, "empty list")
    for j in range(0, len(empty_list)-1):
        board[empty_list[j][0]][empty_list[j][1]] = 0
    return board 








if len(sys.argv) > 1 and sys.argv[1] == "-hint":
    empties = empty_cell_list(grid)
    solution = recursive_solver(grid, explain)
    hint_solution = hint(empties, grid)
    print("new grid")