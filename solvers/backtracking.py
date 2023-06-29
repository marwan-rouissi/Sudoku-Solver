class Backtracking():

    def __init__(self, sudoku:list) -> None:
        self.sudoku = sudoku
        self.puzzleSolution = []
        self.combinaisons = 0
        self.goodone = 0

    """method to check if:
    - for its row (r)
    - for its colomn (c)
    - for its block (j)
    a value is valid or not and return for spot's location its possible values"""
    def check_valid(self, r, c, value):
        not_in_row = value not in self.sudoku[r]
        not_in_column = value not in [self.sudoku[i][c] for i in range(9)]
        not_in_block = value not in [self.sudoku[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
        return not_in_row and not_in_column and not_in_block

    """method to run backtracking.
    for blanks (0s spot) check its valid choices and try it, go to next spot
    if move's not possible, set a 0 and back track to try another possible value
    Do so until last spot and return solution once its all completed """
    def sudoku_back_tracking(self, r=0, c=0):
        if r == 9:
            return True
        elif c == 9:
            return self.sudoku_back_tracking(r+1, 0)
        elif self.sudoku[r][c] != 0:
            return self.sudoku_back_tracking(r, c+1)
        else:
            for value in range(1, 10):
                if self.check_valid(r, c, value):
                    self.sudoku[r][c] = value
                    self.combinaisons += 1
                    # print("------------------")
                    # for row in self.sudoku:
                    #     print(row)
                    if self.sudoku_back_tracking(r, c+1):
                        return True
                    self.sudoku[r][c] = 0
                    self.goodone = self.combinaisons
                    self.puzzleSolution = self.sudoku
            return False