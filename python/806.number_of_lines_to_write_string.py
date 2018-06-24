class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        curr_w = 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            if curr_w + w > 100:
                curr_w = 0
                lines += 1
            curr_w += w
        return [lines, curr_w]
