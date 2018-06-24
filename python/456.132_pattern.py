class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums:
            return False
        cur_min = nums[0]
        cur_max = nums[0]
        interval_tbl = []
        for n in nums:
            if n < cur_min:
                if cur_min != cur_max:
                    while interval_tbl and cur_max >= interval_tbl[-1][0]:
                        cur_max = max(interval_tbl.pop()[1], cur_max)
                    interval_tbl.append((cur_min, cur_max))
                cur_min = cur_max = n
            elif n > cur_min:
                if n < cur_max:
                    print n, cur_max
                    return True
                for min_t, max_t in interval_tbl:
                    if n > min_t and n < max_t:
                        return True
                cur_max = n
        return False
