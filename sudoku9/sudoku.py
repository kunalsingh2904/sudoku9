class Sudoku:
    # @param A : list of list of chars
    # @return nothing
    def __init__(self,board):
        '''
        Input: 2d list --> input board to solve
        '''
        self.__board = list()
        for i in board:
            temp = list(i)
            self.__board.append(temp)
        if len(self.__board) != 9:
            raise Exception("InValid Board. Please give Board of size 9*9")
        for i in self.__board:
            if len(i) != 9:
                raise Exception("InValid Board. Please give Board of size 9*9")
        if not self.IsValidInput(self.__board):
            raise Exception("Given Board is not Valid")

    # output
    def solveSudoku(self):
        self.__solvesudoku()
        out = list()
        for i in self.__board:
            if '.' in i:
                raise Exception("Not Sufficient Data in Board")
            i = "".join(i)
            out.append(i)
        return out

    # check validation of input board
    def IsValidInput(self,A):
        # Determine if a Sudoku is valid
        for i in range(9):      #ROW
            s = set()
            for j in range(9):
                if A[i][j] != ".":
                    if A[i][j] in s:
                        return False
                    else:
                        s.add(A[i][j])
        for i in range(9):      #COL
            s = set()
            for j in range(9):
                if A[j][i] != ".":
                    if A[j][i] in s:
                        return False
                    else:
                        s.add(A[j][i])
        # 3*3 box -->9 box
        arr = list()
        for i in range(3):
            tt = list()
            for j in range(3):
                tt.append(set())
            arr.append(tt)
        for i in range(9):
            for j in range(9):
                ii = i//3
                jj = j//3
                if A[i][j] != ".":
                    if A[i][j] in arr[ii][jj]:
                        return False
                    else:
                        arr[ii][jj].add(A[i][j])
        return True

    def __solvesudoku(self):
        empty = [-1,-1]
        # When no empty positions left then we have our complete sudoku
        if not self.__find_empty_location(empty):
            return True
        
        r,c = empty[0],empty[1]
        
        for num in range(1,10):
            # chekc if our choice of placing num at certain r,c is valid or not
            # print(num)
            if self.__isvalid(num, r, c):
                self.__board[r][c] = str(num)

                if self.__solvesudoku():
                    return True
                # if the taken choice did not yield any solution then backtrack
                self.__board[r][c] = '.'
             
    # function to find empty cell in board   
    def __find_empty_location(self, empty):
        for i in range(9):
            for j in range(9):
                if self.__board[i][j] == '.':
                    empty[0] = i
                    empty[1] = j
                    return True
        return False
    
    # function to check if we can successfully place a number on a particular cell 
    def __isvalid(self, num, r, c):
        # checking if num exists in the corresponding column 
        for i in range(9):
            if self.__board[i][c] == str(num):
                return False
        #checking if num exists in the coresponding row    
        for j in range(9):
            if self.__board[r][j] == str(num):
                return False
        # checking if the number exists in that particular 3X3 block of sudoku 
        r = r-r%3
        c = c-c%3
        for i in range(3): 
            for j in range(3): 
                if self.__board[i+r][j+c] == str(num): 
                    return False
        return True


# if __name__ == '__main__':
#     board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
#     puzzle = Sudoku(board)
#     print(puzzle.solveSudoku())


        
        