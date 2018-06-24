class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        slen = len(seats)
        dp_l = [-1] * slen
        
        l = -1
        for i in range(slen):
            if seats[i]:
                l = i
            dp_l[i] = l

        r = slen
        max_D = 0
        for i in reversed(range(slen)):
            if seats[i]:
                r = i
            else:
                if r == slen:
                    max_D = max(max_D, i - dp_l[i])
                elif dp_l[i] == -1:
                    max_D = max(max_D, r - i)
                else:
                    max_D = max(max_D, min(i - dp_l[i], r - i))
 
        return max_D
