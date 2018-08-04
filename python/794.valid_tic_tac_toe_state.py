class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        o, x = 0, 0
        for row in board:
            for c in row:
                if c == 'O':
                    o += 1
                if c == 'X':
                    x += 1
        if x < o or x > o + 1:
            return False
        
        self.oline, self.xline = 0, 0
        def count_line(c):
            if c == 'O':
                self.oline += 1
            if c == 'X':
                self.xline += 1
        if board[0][0] == board[0][1] == board[0][2]: count_line(board[0][0])
        if board[1][0] == board[1][1] == board[1][2]: count_line(board[1][0])
        if board[2][0] == board[2][1] == board[2][2]: count_line(board[2][0])
        if board[0][0] == board[1][0] == board[2][0]: count_line(board[0][0])
        if board[0][1] == board[1][1] == board[2][1]: count_line(board[0][1])
        if board[0][2] == board[1][2] == board[2][2]: count_line(board[0][2])
        if board[0][0] == board[1][1] == board[2][2]: count_line(board[0][0])
        if board[0][2] == board[1][1] == board[2][0]: count_line(board[0][2])
        
        if self.oline > 0 and self.xline > 0:
            return False
        
        if o == x and self.xline > 0:
            return False
        
        if x > o and self.oline > 0:
            return False
        
        return True
