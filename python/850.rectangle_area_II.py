class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        x_set = set([])
        y_set = set([])
        for x1, y1, x2, y2 in rectangles:
            x_set.add(x1)
            x_set.add(x2)
            y_set.add(y1)
            y_set.add(y2)
        
        x_list = sorted(x_set)
        y_list = sorted(y_set)
        xy_map = [[0] * len(y_list) for _ in range(len(x_list))]
        
        ans = 0
        for x1, y1, x2, y2 in rectangles:
            for i in range(len(x_list) - 1):
                for j in range(len(y_list) - 1):
                    if (x1 <= x_list[i] and
                        x2 >= x_list[i + 1] and
                        y1 <= y_list[j] and
                        y2 >= y_list[j + 1]):
                        if xy_map[i][j]:
                            continue
                        else:
                            ans += (x_list[i] - x_list[i + 1]) * (y_list[j] - y_list[j + 1])
                            xy_map[i][j] = 1
        
        return ans % (pow(10, 9) + 7)
