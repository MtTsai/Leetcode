class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        return self.canMeasureWater_GCD(x, y ,z)
        return self.canMeasureWater_BFS_by_anonymous(x, y ,z)
        return self.canMeasureWater_BFS(x, y ,z)

    # the water can be put in another bucket
    def canMeasureWater_GCD(self, x, y, z):
        def gcd(a, b):
            if a == 0:
                return b
            if b == 0:
                return a
            if a > b:
                return gcd(a % b, b)
            else:
                return gcd(a, b % a)

        if z == 0:
            return True
        if z > x + y:
            return False
        return (z % gcd(x, y)) == 0

    # to avoid recursive too deep rather than DFS
    def canMeasureWater_BFS(self, x, y, z):
        if z == 0:
            return True

        def meas_water(a, b):
            jugs = set([])

            jugs.add((x, b))
            jugs.add((0, b))
            if y - b >= a:
                jugs.add((0, a + b))
            else:
                jugs.add((a - y + b, y))

            jugs.add((a, y))
            jugs.add((a, 0))
            if x - a >= b:
                jugs.add((a + b, 0))
            else:
                jugs.add((x, b - x + a))

            return jugs

        queue = [(0, 0)]
        visited = set((0, 0))
        while queue:
            a, b = queue.pop(0)
            if a + b == z:
                return True

            for pair in meas_water(a, b):
                if pair in visited:
                    continue
                queue.append(pair)
                visited.add(pair)

        return False

    def canMeasureWater_BFS_by_anonymous(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x > y:
            temp = x;
            x = y;
            y = temp;
            
        if z > x + y:
            return False;
        
        # set the initial state will empty jars;
        queue = [(0, 0)];
        visited = set((0, 0));
        while len(queue) > 0:
            a, b = queue.pop(0);
            if a + b == z:
                return True;
            
            states = set()
            
            states.add((x, b)) # fill jar x;
            states.add((a, y)) # fill jar y;
            states.add((0, b)) # empty jar x;
            states.add((a, 0)) # empty jar y;
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a))) # pour jar y to x;
            states.add((0 if a + b < y else a - (y - b), min(b + a, y))) # pour jar x to y;

            for state in states:
                if state in visited:
                    continue;
                queue.append(state)
                visited.add(state);
                
        return False;

if __name__ == "__main__":
    data = [(True,  (3, 5, 4)),
            (False, (2, 6, 5)),
            (True,  (8, 9, 6)),
            (True,  (16, 27, 13)),
            (True,  (22003, 31237, 1)),
            (True,  (104639, 104651, 234))]

    for ans, (x, y, z) in data:
        out = Solution().canMeasureWater(x, y, z)
        if out != ans:
            print "x, y, z: {} {} {}".format(x, y, z)
            print "Expect: {}".format(ans)
            print "Output: {}".format(out)
    print "Done"
