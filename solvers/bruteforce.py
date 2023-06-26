class Bruteforce():

    """Bruteforce object takes a (81 chara) string as parameter"""
    def __init__(self, s:str) -> None:
        self.s = s
        self.puzzleSolution = []
        self.combinaisons = 0
        self.goodone = 0
    
    """method to convert sudoku string to a matrix"""
    def str_to_puzzle(self, s):

        for i in range(len(s)):  
            if i % 9 == 0:
                temp = []
                for j in s[i:i+9]:
                    temp.append(int(j))
                self.puzzleSolution.append(temp)
    
    """method to check if element i and element j are on the same row"""
    def same_row(self, i, j):

        if i//9 == j//9:
            return True
        return False

    """method to check if element i and element j are on the same column"""
    def same_col(self, i, j):

        if i%9 == j%9:
            return True
        return False

    """method to check if element i and element j are on the same block"""
    def same_block(self, i, j):

        if ((i//9)//3 == (j//9)//3) & ((i%9)//3 == (j%9)//3):
            return True
        return False
    
    """method to solve puzzle by checking the sudoku string:
    - find the 1st "0 (i)"
    - for i scan its row/col/block to get determine which values can not be used (cannotuse)
    and its possible values to save them as every_possible_values
    - for localisation i try every possible values 1 by 1
    repeat the 3 steps until no 0 is found and save solution as self.puzzleSolution"""
    def sudoku_brute_force(self, s:str):
        i = s.find('0')

        cannotuse = {s[j] for j in range(len(s)) if self.same_row(i, j) | self.same_col(i, j) | self.same_block(i, j)}
        every_possible_values = {str(i) for i in range(10)} - cannotuse

        for val in every_possible_values:
            s = s[0:i] + val + s[i+1: ]
            self.combinaisons += 1
            self.sudoku_brute_force(s)
            if s.find('0') == -1:
                self.goodone = self.combinaisons
                self.str_to_puzzle(s)