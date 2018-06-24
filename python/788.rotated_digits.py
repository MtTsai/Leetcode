class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N + 1):
            add = 0
            while i:
                if i % 10 in (3, 4, 7):
                    add = 0
                    break
                elif i % 10 in (2, 5, 6, 9):
                    add = 1
                i /= 10
            count += add
        return count
