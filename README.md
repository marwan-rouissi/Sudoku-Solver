# Sudoku-Solver

# Bruteforce vs Backtracking method

| Levels | Field to fill | BrForce possibilities | BkTracking possibilities (solved on) |
| ------ | ------------- | --------------------- | ------------------------------------ |
| lvl 1  | 45            | 319                   | 254 (241th attempt)                  |
| lvl 2  | 52            | 3 239                 | 1 368 (1 355th attempt)              |
| lvl 3  | 43            | 164                   | 117 (97th attempt)                   |
| lvl 4  | 57            | 18 066                | 7 191 (7 172th attempt)              |
| lvl 5  | 58            | 21 135                | 4 262 (4 246th attempt)              |

n = Field to fill

# BruteForce method (Exponential complexity)
 Big O: 
 - O( 10n)

# Backtracking method (Linear complexity)
Big O:
- O( 10xn)
