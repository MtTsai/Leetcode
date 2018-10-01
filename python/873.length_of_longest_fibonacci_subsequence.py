class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.ndict = {}
        for i, n in enumerate(A):
            self.ndict[n] = i
            
        comb = itertools.combinations
        self.dp = [[0] * len(A) for _ in range(len(A))]
        self.dp_dict = {}
        
        def find(i, j):
            # Array DP (FAIL), 2 times long of bfs solution
            if self.dp[i][j]:
                return self.dp[i][j]
            else:
                self.dp[i][j] = 2
                
                k = self.ndict.get(A[i] + A[j], 0)
                if k:
                    self.dp[i][j] = find(j, k) + 1

                return self.dp[i][j]
            # directly bfs (PASS)
            k = self.ndict.get(A[i] + A[j], 0)
            if k:
                return find(j, k) + 1
            else:
                return 2
            # Dict DP will be very slow (FAIL)
            if (i, j) in self.dp_dict.keys():
                return self.dp_dict[(i, j)]
            else:
                self.dp_dict[(i, j)] = 2
                
                k = self.ndict.get(A[i] + A[j], 0)
                if k:
                    self.dp_dict[(i, j)] = find(j, k) + 1

                return self.dp_dict[(i, j)]

        maxSeq = 0
        
        for i, j in comb(range(len(A)), 2):
            maxSeq = max(maxSeq, find(i, j))
        
        return maxSeq if maxSeq > 2 else 0
