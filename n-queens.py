class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.']*n for _ in range(n)]
        visited = set() # check columns
        visited_diagonal = set() # check diagonals
        visited_antidiagonal = set() # check antidiagonals
        def func(row, ans):
            if row == n:
                ans.append([''.join(row) for row in grid])
                return
            for col in range(n):
                diagonal_check = row - col #checking for every diagonal (0,0)-(n-1,n-1)
                antidiagonal_check = row + col # checking for every antidiagonal (0,n-1)- (n-1,0)
            
                if not (col in visited or diagonal_check in visited_diagonal or antidiagonal_check in visited_antidiagonal):
                    visited.add(col)
                    visited_diagonal.add(diagonal_check)
                    visited_antidiagonal.add(antidiagonal_check)
                    grid[row][col] = 'Q'
                    
                    func(row+1, ans)
                    
                    visited.remove(col)
                    visited_diagonal.remove(diagonal_check)
                    visited_antidiagonal.remove(antidiagonal_check)
                    grid[row][col] = '.'
                    
        ans = []
        func(0,ans)
        return ans
      
# Time: O(n!)
# Space: O(n^2)
