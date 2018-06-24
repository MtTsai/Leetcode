class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        while len(ans) <= num:
            ans = ans + [n + 1 for n in ans]
        
        return ans[:num + 1]
