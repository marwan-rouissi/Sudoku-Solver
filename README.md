# Sudoku-Solver

# Bruteforce method

The brute force technique is a generic method for solving puzzles by listing all possible candidate solutions.
It will try all possible combinaisons until it found the right solution, the one fiting with our conditions.
It is not limited to any specific domain of problems and is ideal for solving small and simpler problems.
Brute force algorithms are simple and consistent, but very slow

# Backtracking method

The backtracking method is a depth-first search algorithm that is used to solve puzzles by incrementally building candidates to the solutions and rejecting them as soon as they are found not to satisfy the constraints of the conditions.
It explores every empty fields, check for the possible values and populate it with one of them before to go to the next one.
Once the puzzle is completed, it means a solution is found.
Otherwise, if there's no possible value for the actual empty field to fill, the method backtracks to the previous one and tries another one.

# Bruteforce vs Backtracking

| Levels | Fields to fill | BrForce possibilities | BkTracking possibilities (solved on) |
| ------ | ------------- | ---------------------- | ------------------------------------ |
| lvl 1  | 45            | 319                   | 254 (241th attempt)                   |
| lvl 2  | 52            | 3 239                 | 1 368 (1 355th attempt)               |
| lvl 3  | 43            | 164                   | 117 (97th attempt)                    |
| lvl 4  | 57            | 18 066                | 7 191 (7 172th attempt)               |
| lvl 5  | 58            | 21 135                | 4 262 (4 246th attempt)               |

n = Field to fill

# BruteForce method (Exponential complexity)
 Big O: 
 - O( 10n)

# Backtracking method (Linear complexity)
Big O:
- O( 10xn)
