from solvers.bruteforce import *
from solvers.backtracking import *
from app import *

class Game():
    
    """Game object takes a text file as parameter
    to convert it into a (str) matrix"""
    def __init__(self, sudoku:str) -> None:
        self.sudoku = sudoku
        data = open(self.sudoku, "r")
        self.sudoku = []
        self.numSudoku = []
        row = ""
        self.bla = 0

        for i in data:
            row += i
            self.sudoku.append(list(row))
            row = ""
        for r in self.sudoku:
            if len(r) >9:
                r.pop()
 
        self.convertToNumeric()
        self.s = ''.join(map(str,[''.join(map(str, i)) for i in self.sudoku]))

    """method to convert the string matrix to an integer matrix
    and replace "_" with "0"s"""
    def convertToNumeric(self):
        for row in self.sudoku:
            for col in row:
                i = row.index(col)
                if col == "_":
                    self.bla += 1
                    row[i] = "0"
            res = [eval(col) for col in row]
            self.numSudoku.append(res)

    """method to draw a sudoku game from a matrix"""
    def draw(self, puzzle:list):
        for r in range(len(puzzle)):
            if r == 0 or r == 3 or r == 6:
                print("+-------+-------+-------+")
            for c in range(len(puzzle[r])):
                if c == 0 or c == 3 or c ==6:
                    print("|", end = " ")
                if puzzle[r][c] != 0:
                    # print(f"\033[1;34m")
                    print(puzzle[r][c], end = " ")
                    # print(f"\033[0m")
                else:
                    print(end = "  ")
                if c == 8:
                    print("|")
        print("+-------+-------+-------+")
    
    """method to draw solved puzzle numbers with a different color (green)
    from the auto filled numbers color"""
    def drawSolvedPuzzle(self, puzzle):
        for r in range(len(puzzle)):
            if r == 0 or r == 3 or r == 6:
                print("+-------+-------+-------+")
            for c in range(len(puzzle[r])):
                if c == 0 or c == 3 or c ==6:
                    print("| ", end = "")

                if puzzle[r][c] != int(self.sudoku[r][c]):
                    print(f"\033[1;32m{puzzle[r][c]}\033[0m", end = " ")
                else:
                    print(puzzle[r][c], end = " ")
                if c == 8:
                    print("|")
        print("+-------+-------+-------+")
    
    "method to run the brute force method from Bruteforce class"
    def run_bruteforce(self):
        bruteForce = Bruteforce(self.s)
        bruteForce.sudoku_brute_force(game.s)
        print("--------------")
        print("SOLVED PUZZLE")
        print("BRUTE FORCE")
        print("--------------")
        self.drawSolvedPuzzle(bruteForce.puzzleSolution)
        print(f"{bruteForce.combinaisons} possible combinaisons")
        print(f"found on {bruteForce.goodone}th attempt")

        return bruteForce.puzzleSolution
    
    "method to run the back tracking method from Backtracking class"
    def run_backtracking(self):
        backtracking = Backtracking(game.numSudoku)
        backtracking.sudoku_back_tracking()
        print("--------------")
        print("SOLVED PUZZLE")
        print("BACK TRACKING")
        print("--------------")
        self.drawSolvedPuzzle(backtracking.puzzleSolution)
        print(f"{backtracking.combinaisons} possible combinaisons")
        print(f"found on {backtracking.goodone}th attempt")


level_1 = "puzzles/sudoku.txt"
level_2 = "puzzles/sudoku2.txt"
level_3 = "puzzles/sudoku3.txt"
level_4 = "puzzles/sudoku4.txt"
level_5 = "puzzles/evilsudoku.txt"

"""convert user's input into a variable to select the puzzle to solve"""
def convertInput(s):
    if s == "1":
        s = level_1
    if s == "2":
        s = level_2
    if s == "3":
        s = level_3
    if s == "4":
        s = level_4
    if s == "5":
        s = level_5
    return s

if __name__ == "__main__":
    print("What level to solve ? (1-5)")
    choiceLvl = input()
    convertInput(choiceLvl)

    game = Game(convertInput(choiceLvl))
    print("--------------")
    print("PUZZLE TO SOLVE")
    print("--------------")
    game.draw(game.numSudoku)
    # app.run_pygame()
    print("which method do you want to use ? (bruteforce / backtracking)")
    methodChoice = input()
    if methodChoice == "bruteforce":
        game.run_bruteforce()
        soluce = game.run_bruteforce()
    if methodChoice == "backtracking":
        game.run_backtracking()
        soluce = game.numSudoku
    
    print(f"field to fill = {game.bla}")
    
    app = App(game.sudoku, soluce)
    app.run_pygame()