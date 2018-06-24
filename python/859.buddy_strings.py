class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A != B:
            diff = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    diff.append(i)
                if len(diff) > 2:
                    return False
            if len(diff) == 1:
                return False
            else:
                return (A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]])
        else:
            cdict = {}
            for c in A:
                if c in cdict.keys():
                    cdict[c] += 1
                    if cdict[c] >= 2:
                        return True
                else:
                    cdict[c] = 1
            return False
