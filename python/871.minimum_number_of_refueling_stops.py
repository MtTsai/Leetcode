class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # Priority Queue
        
        slen = len(stations)

        fuel = startFuel
        stop = -1
        fuel_queue = []
        stopcnt = 0
        while fuel < target:
            for i in range(stop + 1, slen):
                if stations[i][0] <= fuel:
                    fuel_queue.append(stations[i][1])
                    stop = i

            fuel_queue.sort()
            
            if not len(fuel_queue):
                return -1
            fuel += fuel_queue.pop(-1)
            stopcnt += 1
            
        return stopcnt
        
        # BF
        
        slen = len(stations)
        
        self.min_refuel = float('inf')
        def dfs(start, fuel, depth):
            if start + fuel >= target:
                self.min_refuel = min(self.min_refuel, depth)

            for i in range(slen):
                if (stations[i][0] > start and
                    stations[i][0] <= start + fuel):
                    dfs(stations[i][0], start + fuel - stations[i][0] + stations[i][1], depth + 1)
        
        dfs(0, startFuel, 0)
        return self.min_refuel if self.min_refuel != float('inf') else -1
        
        
        # DP
        
        slen = len(stations)

        dp = {}
        def dfs(start, fuel):
            key = (start, fuel)
            if start + fuel >= target:
                dp[key] = 0
            if key in dp.keys():
                return dp[key]
            else:
                dp[key] = float('inf')
                
                for i in range(slen):
                    if (stations[i][0] > start and
                        stations[i][0] <= start + fuel):
                        dp[key] = min(dp[key], dfs(stations[i][0], start + fuel - stations[i][0] + stations[i][1]) + 1)

                return dp[key]
        
        dfs(0, startFuel)
        
        return dp[(0, startFuel)] if dp[(0, startFuel)] != float('inf') else -1
