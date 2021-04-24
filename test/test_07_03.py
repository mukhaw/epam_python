import numpy as np

from hm_1.tasks.task_07_03 import tic_tac_toe_checker


def test_tic_tac_toe_returns_unfinished():
    board = np.array([["-", "-", "o"], ["-", "o", "o"], ["-", "x", "x"]])
    assert tic_tac_toe_checker(board) == "unfinished"


def test_tic_tac_toe_returns_o_wins():
    board = np.array([["-", "-", "o"], ["-", "o", "o"], ["-", "x", "o"]])
    assert tic_tac_toe_checker(board) == "o wins"


def test_tic_tac_toe_returns_x_wins():
    board = np.array([["x", "-", "o"], ["-", "x", "o"], ["-", "x", "x"]])
    assert tic_tac_toe_checker(board) == "x wins"
