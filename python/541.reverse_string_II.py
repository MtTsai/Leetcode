class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        slen = len(s)
        rev = 1
        ans = ""
        for i in range(((slen - 1) / k) + 1):
            start, end = i * k, min(slen, (i + 1) * k)
            temp = s[start:end]
            ans += temp[::-1] if rev else temp
            rev ^= 1
        return ans
