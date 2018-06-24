class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nlen = len(nums)
        
        def findInsertPos(left, right):
            if left == right:
                return left
            
            mid = (left + right) / 2
            if nums[mid] >= target:
                return findInsertPos(left, mid)
            else:
                return findInsertPos(mid + 1, right)

        return findInsertPos(0, nlen)
