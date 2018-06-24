class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def findscore(string):
            if len(string) == 2:
                return 1
            ret, l, r, start = 0, 0, 0, 1
            for i in range(1, len(string) - 1):
                if string[i] == '(':
                    l += 1
                else:
                    r += 1
                if l == r:
                    ret += findscore(string[start:i + 1])
                    start = i + 1
            return ret * 2

        ret, l, r, start = 0, 0, 0, 0
        for i in range(len(S)):
            if S[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ret += findscore(S[start:i + 1])
                start = i + 1
        return ret
                
                
