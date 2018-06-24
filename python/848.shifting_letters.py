class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        def shift(c, n):
            t = ord(c) + n
            while t > ord('z'):
                t -= 26
            return chr(t)
        
        accu = 0
        ans = ''
        for i in reversed(range(len(shifts))):
            accu = (accu + shifts[i]) % 26
            ans = shift(S[i], accu) + ans
            
        return ans
