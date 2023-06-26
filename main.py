from solvers.bruteforce import *

class Game():
    
    """Game object takes a text file as parameter
    to convert it into a (str) matrix"""
    def __init__(self, sudoku:str) -> None:
        self.sudoku = sudoku

        data = open(self.sudoku, "r")
        self.sudoku = []
        self.numSudoku = []
        row = ""

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
                    print("| ", end = "")
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

                if puzzle[r][c] != self.numSudoku[r][c]:
                    print(f"\033[1;32m{puzzle[r][c]}\033[0m", end = " ")
                else:
                    print(puzzle[r][c], end = " ")
                if c == 8:
                    print("|")
        print("+-------+-------+-------+")
    
    "method to run the brute force method from Bruteforce class"
    def run_bruteforce(self):
        print("--------------")
        print("PUZZLE TO SOLVE")
        print("--------------")
        game.draw(game.numSudoku)

        bruteForce = Bruteforce(self.s)
        bruteForce.sudoku_brute_force(game.s)
        print("--------------")
        print("SOLVED PUZZLE")
        print("--------------")
        self.drawSolvedPuzzle(bruteForce.puzzleSolution)
        print(f"{bruteForce.combinaisons} possible combinaisons")
        print(f"found on {bruteForce.goodone}th attempt")
    

level_1 = "puzzles/sudoku.txt"
level_2 = "puzzles/sudoku2.txt"
level_3 = "puzzles/sudoku3.txt"
level_4 = "puzzles/sudoku4.txt"
level_5 = "puzzles/evilsudoku.txt"

game = Game(level_5)

if __name__ == "__main__":
    game.run_bruteforce()