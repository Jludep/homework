from task03 import tic_tac_toe_checker

class TestTicTacToeChecker:
    def test_x_wins_row(self):
        board = [['X', 'X', 'X'], ['O', 'O', '-'], ['-', '-', '-']]
        assert tic_tac_toe_checker(board) == 'X wins'

    def test_o_wins_column(self):
        board = [['O', 'X', 'O'], ['O', 'X', '-'], ['O', '-', 'X']]
        assert tic_tac_toe_checker(board) == 'O wins'

    def test_x_wins_diagonal(self):
        board = [['O', 'X', 'X'], ['-', 'X', '-'], ['O', '-', '-']]
        assert tic_tac_toe_checker(board) == 'X wins'

    def test_unfinished_board(self):
        board = [['O', '-', 'X'], ['-', 'O', '-'], ['-', '-', '-']]
        assert tic_tac_toe_checker(board) == 'the board is unfinished'

    def test_draw(self):
        board = [['O', 'X', 'O'], ['O', 'X', 'X'], ['X', 'O', 'O']]
        assert tic_tac_toe_checker(board) == "it's a draw"
