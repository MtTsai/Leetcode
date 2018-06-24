class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for idx, n in enumerate(nums):
            coml = target - n
            if coml in m.keys():
                return [m[coml], idx]
            m[n] = idx
