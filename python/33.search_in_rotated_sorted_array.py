class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nlen = len(nums)
        if not nlen:
            return -1

        if nlen == 1:
            return 0 if nums[0] == target else -1

        start = 0
        l_bound, r_bound = 0, nlen - 1

        # find start until start less than the left one (the minimal one)
        while nums[start] >= nums[((start - 1) + nlen) % nlen]:
            if nums[start] >= nums[nlen - 1]:
                # find right side
                l_bound = start
                start = start + ((r_bound - start + 1) / 2)
            else:
                # find left side
                r_bound = start
                start = start - ((start - l_bound + 1) / 2)

        nums = nums[start:] + nums[:start]

        find = 0
        l_bound, r_bound = 0, nlen -1

        while nums[find] != target:
            if nums[find] < target:
                # find right side
                l_bound = find
                find = find + ((r_bound - find + 1) / 2)

                # already find the right one
                if find >= r_bound:
                    break
            else:
                # find left side
                r_bound = find
                find = find - ((find - l_bound + 1) / 2)

                # already find the left one
                if find <= l_bound:
                    break

        # rotate with pivot for original nums
        return (find + start) % nlen if nums[find] == target else -1

if __name__ == "__main__":
    data = [(-1, [],                    5),
            (1,  [1, 3],                3),
            (2,  [4, 5, 6, 7, 0, 1, 2], 6),
            (-1, [4, 5, 6, 7, 0, 1, 2], 3),
            (0,  [6, 7, 0, 1, 2, 3, 4], 6),
            (-1, [6, 7, 0, 1, 2, 3, 4], 5),
            (-1, [6, 7, 0, 1, 2, 4, 5], 3)]

    for ans, array, target in data:
        out = Solution().search(array, target)
        if ans != out:
            print "array, target: {}, {}".format(array, target)
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
