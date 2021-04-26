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
    for i in range(len(board)):
        yield [row[i] for row in board]


def diagonals(board):
    n = list(range(len(board)))
    return [
        [board[i][i] for i in range(len(board))],
        [board[i][j] for i, j in zip(n, reversed(n))],
    ]


def winner(row):
    row = "".join(row)
    if row == "xxx":
        return "x wins"
    if row == "ooo":
        return "o wins"
    return ""


def tic_tac_toe_checker(board) -> str:
    res = ""
    for i in board:
        res += winner(i)
    for i in list(transponse(board)):
        if winner(i) not in res:
            res += winner(i)
    for i in diagonals(board):
        if winner(i) not in res:
            res += winner(i)
    if len(res) > 6:
        return "draw"
    elif not res:
        return "unfinished"
    else:
        return res
