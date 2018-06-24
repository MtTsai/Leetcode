class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        qlen = len(quiet)
        richer_list = [set([]) for i in range(qlen)]
        dp_rs = [0] * qlen
        
        for x, y in richer:
            richer_list[y].add(x)
        
        ans = [0] * qlen
        
        def find_rs(i, l):
            if type(dp_rs[i]) != set:
                rs = set([_ for _ in l[i]])
                for p in l[i]:
                    rs |= find_rs(p, l)
                dp_rs[i] = rs
            return dp_rs[i]
        
        for i in range(qlen):
            qr = quiet[i]
            rr = i
            for p in find_rs(i, richer_list) | set([i]):
                if quiet[p] < qr:
                    qr = quiet[p]
                    rr = p
            ans[i] = rr
        return ans
        
