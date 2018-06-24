class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        station_nums = len(gas)
        
        gas_tank = 0
        arrive = -1
        for sid in range(station_nums):
            
            while gas_tank >= 0 and arrive < station_nums - 1:
                arrive += 1
                station = (sid + arrive) % station_nums
                gas_tank = gas_tank + gas[station] - cost[station]
                
            
            if arrive == station_nums - 1 and gas_tank >= 0:
                return sid
            else:
                gas_tank = gas_tank - gas[sid] + cost[sid]
                arrive -= 1
            
        return -1
