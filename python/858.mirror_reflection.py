class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        
        x = p
        y = q
        UP, DOWN = 0, 1
        y_dir = UP
        
        while True:
            x ^= p
            if y_dir == UP:
                y += q
                if y > p:
                    y_dir = DOWN
                    y = p - (y - p)
            else:
                y -= q
                if y < 0:
                    y_dir = UP
                    y = 0 - y
        
        
            if x == p and y == 0:
                return 0
            elif x == p and y == p:
                return 1
            elif x == 0 and y == p:
                return 2
        
