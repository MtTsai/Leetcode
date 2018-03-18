class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nlen = len(nums)

        l_p = [0] * nlen
        r_p = [0] * nlen

        product = 1
        for idx in range(nlen):
            l_p[idx] = product
            product *= nums[idx]

        product = 1
        for idx in reversed(range(nlen)):
            r_p[idx] = product
            product *= nums[idx]

        return [l_p[idx] * r_p[idx] for idx in range(nlen)]

if __name__ == "__main__":
    data = [([24, 12, 8, 6], [1, 2, 3, 4])]

    for ans, array in data:
        out = Solution().productExceptSelf(array)
        if ans != out:
            print "array: {}".format(array)
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
