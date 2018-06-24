class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        digit = []
        while N:
            digit.append(N % 10)
            N /= 10

        pend = -1 # start to pend 9
        
        for i in range(len(digit) - 1):
            if digit[i] < digit[i + 1]:
                digit[i + 1] -= 1
                pend = i
        ans = 0
        for i in reversed(range(len(digit))):
            ans = ans * 10 + (digit[i] if i > pend else 9)

        return ans
