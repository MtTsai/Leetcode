class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            change[bill] += 1
            if bill == 20:
                if change[10]:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
            elif bill == 10:
                change[5] -= 1

            if change[5] < 0:
                return False
        return True        
