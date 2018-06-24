class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end_pos = len(nums) - 1
        curr_pos = 0
        far_pos = nums[0]
        step = 0
        
        while curr_pos < end_pos:
            max_pos = far_pos
            for i in range(curr_pos + 1, min(end_pos, far_pos) + 1):
                max_pos = max(max_pos, i + nums[i])

            curr_pos, far_pos = far_pos, min(len(nums) - 1, max_pos)
            step += 1
        
        return step
