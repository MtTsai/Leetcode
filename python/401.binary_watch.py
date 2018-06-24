class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        bit_arr = [[],[],[],[],[],[]]
        for v in range(60):
            bit = 0
            v_t = v
            while v_t:
                if v_t & 1:
                    bit += 1
                v_t >>= 1
            bit_arr[bit].append(v)
        ans = []
        for hled in range(num + 1):
            mled = num - hled
            if hled > 3 or mled > 5:
                continue
            for h in bit_arr[hled]:
                if h > 11:
                    continue
                for m in bit_arr[mled]:
                    if m < 10:
                        ans.append(str(h) + ':0' + str(m))
                    else:
                        ans.append(str(h) + ':' + str(m))
        return ans

            
