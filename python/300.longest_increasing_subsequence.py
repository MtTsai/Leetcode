class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hist = [] # index is sub_seq len, content is heading value
        for i in nums:
            idx = 0

            while idx < len(hist):
                # if i < heading value
                # replace the heading value of sub_seq len
                if i <= hist[idx]:
                    hist[idx] = i
                    break
                idx += 1

            if idx == len(hist):
                hist.append(i)

        return len(hist)

if __name__ == "__main__":
    data = [(4, [10, 9, 2, 5, 3, 7, 101, 18]),
            (3, [10, 9, 2, 5, 3, 4])]

    for ans, seq in data:
        out = Solution().lengthOfLIS(seq)
        if ans != out:
            print "seq: {}".format(seq)
            print "output: {}".format(out)
            print "expect: {}".format(ans)
    print "Done"
