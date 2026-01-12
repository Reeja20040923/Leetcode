class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)

                    square_id = i//3*3+j//3
                    squares[square_id].add(num)
#defining backtracking
        def backTrack(i,j):
            nonlocal solved
            if i==9:
                solved = True
                return

            new_i = i+(j+1)//9
            new_j = (j+1)%9

            if board[i][j] != ".":
                backTrack(new_i,new_j) 

            else :
                for num in range(1,10):
                    square_id = i//3*3+j//3
                    if num not in rows[i] and num not in cols[j] and num not in squares[square_id]:
                        rows[i].add(num)
                        cols[j].add(num)
                        squares[square_id].add(num)
                        board[i][j] = str(num)

                        backTrack(new_i,new_j)

                        if not solved:
                            rows[i].remove(num)
                            cols[j].remove(num)
                            squares[square_id].remove(num)
                            board[i][j] = "."


        solved = False
        backTrack(0,0)

