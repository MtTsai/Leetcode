class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nlen = len(nums)
        dp = [0] * nlen

        ptr = nlen - 1
        for pos in reversed(range(nlen)):
            if pos + nums[pos] >= ptr:
                ptr = pos

        return ptr == 0

if __name__ == "__main__":
    data = [(True,  [2, 3, 1, 1, 4]),
            (False, [3, 2, 1, 0, 4]),
            (True,  [1, 2, 3]),
            (True,  [1, 1, 1, 0]),
            (True,  [1] * 25000),
            (False, [n for n in reversed(range(25001))] + [0])]

    for ans, array in data:
        out = Solution().canJump(array)
        if ans != out:
            print "array: {}".format(array)
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
