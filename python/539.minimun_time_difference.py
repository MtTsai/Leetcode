class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        l = [int(time[:2]) * 60 + int(time[-2:]) for time in timePoints]
        
        mindiff = 12 * 60
        sl = sorted(l)
        
        for idx in range(len(sl) - 1):
            tdiff = sl[idx + 1] - sl[idx]
            if tdiff > 12 * 60:
                tdiff = 24 * 60 - tdiff
            mindiff = min(mindiff, tdiff)
        tdiff = sl[-1] - sl[0]
        if tdiff > 12 * 60:
            tdiff = 24 * 60 - tdiff
        mindiff = min(mindiff, tdiff)
        return mindiff
