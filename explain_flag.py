# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:54:15 2023

@author: charl
"""

def explain(board, empty_list):
    for pos in range(0, len(empty_list)):
        answer = board[empty_list[pos][0][empty_list[pos][1]]]
        row_val = empty_list[pos][0]
        col_val = empty_list[pos][1]
        print("Put",answer,"in location","(",row_val,",",col_val,")")