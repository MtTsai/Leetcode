class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        tlen = len(A)
        
        sA = sorted(range(len(A)), key=lambda k: A[k])
        sB = sorted(range(len(B)), key=lambda k: B[k])
        
        ib = 0
        outmap = [-1] * tlen
        
        for ia in range(tlen):
            if B[sB[ib]] < A[sA[ia]]:
                outmap[ia] = ib
                ib += 1
        
        out = [-1] * tlen
        remain = []
        for ia in range(tlen):
            if outmap[ia] >= 0:
                out[sB[outmap[ia]]]= A[sA[ia]]
            else:
                remain.append(A[sA[ia]])

        for ia in range(tlen):
            if out[ia] < 0:
                out[ia]= remain.pop()
        
        return out
