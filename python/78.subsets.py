class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def sub(l):
            ret = [[]]
            for i, n in enumerate(l):
                ret += [[n] + subl for subl in sub(l[i + 1:])]
            return ret

        return sub(nums)
