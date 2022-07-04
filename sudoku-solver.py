def issafe(row, col, c):
            row, col = int(row), int(col)
            for i in range(9): 
                if board[i][col]== c: return False
                if board[row][i]== c: return False
                if board[3*(row//3) + i//3][3*(col//3) + i%3]== c: return False
            return True
        n = len(board)
        def backtrack(i,j):
            if i== n: return True
            if j == n: return backtrack(i+1, 0)
            #for i in range(len(board)):
            #    for j in range(len(board[0])):

            if board[i][j]== '.':
                for c in range(1,10):
                    if issafe(i, j, str(c)):
                        board[i][j]= str(c)

                        if backtrack(i, j+1):
                        #if backtrack(board):
                            return True
                        else:
                            board[i][j]= "."
                return False
            else:
                return backtrack(i,j+1)
        backtrack(0,0)
        
# Time: O(9^(n^2)) #since in worst case there would be 9 possibilities for n^2 board
# Space: O(1) # We are modifying the original matrix
