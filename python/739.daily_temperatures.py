class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        queue = []
        out = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            t_curr = temperatures[i]
            for (t, j) in reversed(queue):
                if t_curr <= t:
                    break
                else:
                    queue.pop(-1)
                    out[j] = i - j
            queue.append((t_curr, i))
        return out
