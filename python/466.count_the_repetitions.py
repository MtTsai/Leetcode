class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """

        i1 = i2 = r = 0
        last_i2 = -1
        tbl = []
        circulation = False
        while r < n1:
            if s1[i1] == s2[i2]:
                i2 += 1
                if i2 == len(s2):
                    tbl.append((i1, r))
                    i2 = 0
                    last_i2 = -1

                    if len(tbl) > 1 and i1 == tbl[0][0]: # circulation
                        circulation = True
                        break
            i1 += 1
            if i1 == len(s1):
                r += 1
                i1 = 0
                # prevent not found
                if i2 == last_i2:
                    return 0
        if circulation:
            base_r = tbl[0][1]
            last_r = tbl[-1][1]
            around = last_r - base_r

            times = ((n1 - 1 - base_r) / around) * (len(tbl) - 1) + 1
            remain_r = (n1 - 1 - base_r) % around

            for i, r in tbl[1:]: # skip base
                if remain_r >= (r - base_r):
                    times += 1
            return times / n2
        else:
            return len(tbl) / n2

if __name__ == "__main__":
    data = [(2, "acb", 4, "ab", 2),
            (1, "aabc", 3, "aba", 2),
            (1, "aabc", 1, "aabc", 1),
            (1, "acb", 1, "acb", 1),
            (2, "bacaba", 3, "abacab", 1),
            (4, "aaa", 3, "aa", 1),
            (12, "aaa", 20, "aaaaa", 1),
            (2, "aahumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenazkycxf", 1000000, "aac", 1000000)]

    for ans, s1, n1, s2, n2 in data:
        out = Solution().getMaxRepetitions(s1, n1, s2, n2)
        if out != ans:
            print "S1: {} * {}, S2: {} * {}".format(s1, n1, s2, n2)
            print "Expect: {}".format(ans)
            print "Output: {}".format(out)
    print "Done"
