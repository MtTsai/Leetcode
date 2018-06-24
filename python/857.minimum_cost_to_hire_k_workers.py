class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        class ST(object):
            def __init__(self, ratio, quality):
                self.ratio = ratio
                self.quality = quality
            def __str__(self):
                return str(self.ratio)
                
        wlen = len(quality)
        st_list = []
        for i in range(wlen):
            st_list.append(ST(float(wage[i]) / quality[i], quality[i]))

        sort_st = sorted(st_list, key=lambda t: t.ratio)
        sumq = 0
        paid = 0
        heap = []
        for i in range(wlen):
            sumq += sort_st[i].quality
            heap.append(sort_st[i].quality)
            heap.sort(reverse = True)
            if i >= K:
                sumq -= heap[0]
                heap.pop(0)
            if i + 1 >= K:
                
                if not paid:
                    paid = sumq * sort_st[i].ratio
                else:
                    paid = min(paid, sumq * sort_st[i].ratio)
            
        return paid

