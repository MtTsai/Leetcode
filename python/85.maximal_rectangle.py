#!/bin/env python

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        ly = len(matrix)
        lx = len(matrix[0]) if ly > 0 else 0

        if not lx:
            return 0

        xlist = [0] * lx
        max_area = 0

        for row in matrix:
            for i in range(lx):
                if row[i] == '1':
                    xlist[i] += 1
                else:
                    xlist[i] = 0

            for i in range(lx):
                col, max_h = i, xlist[i]

                if not max_h:
                    continue

                # calc area here
                h = 1
                while h <= max_h:
                    col_r = col + 1
                    area = h
                    while col_r < lx:
                        if xlist[col_r] >= h:
                            area += h
                            col_r += 1
                        else:
                            break

                    if area > max_area:
                        max_area = area

                    h += 1


        return max_area

    def _maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        ly = len(matrix)
        lx = len(matrix[0]) if ly > 0 else 0

        xlist = {}
        max_area = 0

        for row in matrix:
            is_1 = False
            start_1 = 0
            klist = []
            for i in range(lx):
                if is_1 and row[i] == '0':
                    for si in range(start_1, i):
                        for sj in range(si, i):
                            klist.append((si, sj))
                    is_1 = False
                elif not is_1 and row[i] == '1':
                    is_1 = True
                    start_1 = i
            if is_1:
                for si in range(start_1, lx):
                    for sj in range(si, lx):
                        klist.append((si, sj))

            for key_o in xlist.keys():
                if key_o not in klist:
                    new_area = xlist[key_o] * (key_o[1] - key_o[0] + 1)
                    # print (key_o, xlist[key_o], new_area, max_area)
                    if new_area > max_area:
                        max_area = new_area
                    del xlist[key_o]

            for key_n in klist:
                if key_n in xlist.keys():
                    xlist[key_n] += 1
                else:
                    xlist[key_n] = 1

        for key, height in xlist.iteritems():
            new_area = xlist[key] * (key[1] - key[0] + 1)
            # print (key, xlist[key], new_area, max_area)
            if new_area > max_area:
                max_area = new_area

        return max_area

if __name__ == '__main__':
    mats = [(0, []),
            (0, [['0']]),
            (6, [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]),
            (6, [['0', '0', '1', '1', '0'],
                 ['1', '0', '1', '1', '0'],
                 ['0', '1', '1', '0', '1'],
                 ['0', '1', '1', '0', '1'],
                 ['0', '0', '1', '0', '1'],
                 ['0', '0', '1', '1', '1']])]

    for (ans, mat) in mats:
        area = Solution().maximalRectangle(mat)
        if area != ans:
            print "Fail in {} != {} {}".format(area, ans, mat)

    print "Done"


