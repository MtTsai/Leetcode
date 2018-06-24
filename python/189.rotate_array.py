class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        nlen = len(nums)
        rotate = k % nlen
        nums[:] = nums[-rotate:] + nums[:-rotate]
