class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        tbl = [0] * 10000
        for v in deck:
            tbl[v] += 1

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        X = 0
        for v in tbl:
            if not v:
                continue
            if not X:
                X = v
            else:
                X = gcd(v, X)
                if X < 2:
                    break
        return (X >= 2)
