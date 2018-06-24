# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        def findFirstBadVersion(left, right):
            if left + 1 >= right:
                return left if isBadVersion(left) else right

            mid = (left + right) / 2
            if isBadVersion(mid):
                return findFirstBadVersion(left, mid)
            else:
                return findFirstBadVersion(mid + 1, right)

        return findFirstBadVersion(1, n)
