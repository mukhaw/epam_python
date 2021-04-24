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


def transponse(board):
    transponse_list = []
    for i in range(len(board)):
        transponse_list.append([row[i] for row in board])
    return transponse_list


def diagonals(board):
    n = list(range(len(board)))
    return [
        [board[i][i] for i in range(len(board))],
        [board[i][j] for i, j in zip(n, reversed(n))],
        ["-", "-", "-"],
    ]


def tic_tac_toe_checker(board) -> str:
    for i, j, k in zip(board, transponse(board), diagonals(board)):
        if "".join(i) == "xxx" or "".join(j) == "xxx" or "".join(k) == "xxx":
            return "x wins"
        if "".join(i) == "ooo" or "".join(j) == "ooo" or "".join(k) == "ooo":
            return "o wins"
    return "unfinished"
