from hm_1.tasks.task_07_03 import tic_tac_toe_checker


def test_tic_tac_toe_returns_unfinished():
    board = [["-", "-", "o"], ["-", "o", "o"], ["-", "x", "x"]]
    assert tic_tac_toe_checker(board) == "unfinished"


def test_tic_tac_toe_returns_o_wins():
    board = [["-", "-", "o"], ["-", "o", "o"], ["o", "x", "x"]]
    assert tic_tac_toe_checker(board) == "o wins"


def test_tic_tac_toe_returns_x_wins():
    board = [["x", "-", "o"], ["-", "x", "o"], ["-", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins"


def test_tic_tac_toe_returns_draw():
    board = [["x", "x", "o"], ["-", "x", "o"], ["-", "x", "o"]]
    assert tic_tac_toe_checker(board) == "draw"


def test_tic_tac_toe_returns_x_wins_with_columns():
    board = [["o", "x", "o"], ["-", "x", "o"], ["-", "x", "x"]]
    board_1 = [["x", "o", "o"], ["x", "-", "o"], ["x", "-", "x"]]
    board_2 = [["x", "o", "o"], ["x", "-", "o"], ["x", "-", "x"]]

    assert tic_tac_toe_checker(board) == "x wins"
    assert tic_tac_toe_checker(board_1) == "x wins"
    assert tic_tac_toe_checker(board_2) == "x wins"


def test_tic_tac_toe_returns_x_wins_with_rows():
    board = [["x", "x", "x"], ["-", "x", "o"], ["-", "o", "o"]]
    board_1 = [["x", "o", "o"], ["x", "x", "x"], ["o", "-", "-"]]
    board_2 = [["x", "o", "o"], ["o", "-", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(board) == "x wins"
    assert tic_tac_toe_checker(board_1) == "x wins"
    assert tic_tac_toe_checker(board_2) == "x wins"
