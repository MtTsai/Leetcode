class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        remains = {}
        
        for i, n in enumerate(numbers):
            if n in remains.keys():
                return [remains[n] + 1, i + 1]
            else:
                remains[target - n] = i
