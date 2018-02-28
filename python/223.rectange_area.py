# 223. REctangle Area

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        _U, _D, _L, _R, _O = 1, 2, 3, 4, 5
        x = y = 0

        # E or G between A - C
        if E < A and G > C:
            x = _O
        else:
            if E >= A and E <= C:
                x += _L
            if G >= A and G <= C:
                x += _R

        # F or H between B - D
        if F < B and H > D:
            y = _O
        else:
            if F >= B and F <= D:
                y += _D
            if H >= B and H <= D:
                y += _U

        lx = ly = 0
        # find x overlap len
        if x == _O:
            lx = C - A
        if x == _L:
            lx = C - E
        if x == _R:
            lx = G - A
        if x == _L + _R:
            lx = G - E

        # find y overlap len
        if y == _O:
            ly = D - B
        if y == _U:
            ly = H - B
        if y == _D:
            ly = D - F
        if y == _U + _D:
            ly = H - F

        return - lx * ly + (C - A) * (D - B) + (G - E) * (H - F)
