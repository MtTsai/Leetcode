class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not k:
            return []
        ans = []
        max_i = -1
        for i in range(len(nums) - k + 1):
            if max_i < i:
                max_i = i
                local_max = nums[max_i]
                for j in range(max_i, i + k):
                    if nums[j] > local_max:
                        local_max = nums[j]
                        max_i = j
            else:
                local_max = nums[max_i]
                if nums[i + k - 1] > local_max:
                    local_max = nums[i + k - 1]
                    max_i = i + k - 1
            ans.append(local_max)
        return ans
                
 
