class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if not N:
            return False

        pow2_list = [[] for _ in range(11)]
        pow2 = 1
        while pow2 <= 1000000000:
            pow2_list[len(str(pow2))].append(str(pow2))
            pow2 <<= 1

        strn = str(N)
        nlen = len(strn)
        
        l = pow2_list[nlen]
        
        for valid in l:
            is_find = True
            for d in set(valid):
                cnt1, cnt2 = 0, 0
                for c in strn:
                    if c == d:
                        cnt1 += 1
                for c in valid:
                    if c == d:
                        cnt2 += 1
                if cnt1 != cnt2:
                    is_find = False
            if is_find:
                return True
            
        return False
