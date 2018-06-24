class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = {}
        for n in answers:
            count[n] = count.get(n, 0) + 1

        out = 0
        for k in count.keys():
            times = count[k] / (k + 1)
            times += 1 if count[k] % (k + 1) else 0
            out += times * (k + 1)
        
        return out

