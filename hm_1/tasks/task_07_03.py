"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
import numpy as np


def tic_tac_toe_checker(board) -> str:
    diagonals = [np.fliplr(board).diagonal(), board.diagonal(), ["-", "-", "-"]]
    for i, j, k in zip(board, board.transpose(), diagonals):
        if "".join(i) == "xxx" or "".join(j) == "xxx" or "".join(k) == "xxx":
            return "x wins"
        if "".join(i) == "ooo" or "".join(j) == "ooo" or "".join(k) == "ooo":
            return "o wins"
    return "unfinished"
