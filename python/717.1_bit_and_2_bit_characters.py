class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        i = 0
        for n in reversed(bits[:-1]):
            if not n:
                break
            else:
                i += 1
        
        return i % 2 == 0
