class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0]) if m else 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] & 1:
                    if i > 0 and j > 0:
                        board[i - 1][j - 1] += 2
                    if j > 0:
                        board[i][j - 1] += 2
                    if i < m - 1 and j > 0:
                        board[i + 1][j - 1] += 2
                    if i > 0:
                        board[i - 1][j] += 2
                    if i < m - 1:
                        board[i + 1][j] += 2
                    if i > 0 and j < n - 1:
                        board[i - 1][j + 1] += 2
                    if j < n - 1:
                        board[i][j + 1] += 2
                    if i < m - 1 and j < n - 1:
                        board[i + 1][j + 1] += 2

        for i in range(m):
            for j in range(n):
                live = board[i][j] >> 1
                if board[i][j] & 1:
                    board[i][j] = 1 if live == 2 or live == 3 else 0
                else:
                    board[i][j] = 1 if live == 3 else 0

