class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if not len(A):
            return True
        
        for i in range(len(B)):
            if A == B[i:] + B[:i]:
                return True
        return False
