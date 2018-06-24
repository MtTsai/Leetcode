class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def cas(st):
            say = ''
            ch = st[0]
            count = 1
            for c in st[1:]:
                if c != ch:
                    say += str(count) + ch
                    ch = c
                    count = 1
                else:
                    count += 1
            say += str(count) + ch
            return say
        ret = '1'
        for _ in range(n - 1):
            ret = cas(ret)
        return ret
