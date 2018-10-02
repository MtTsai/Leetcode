class StockSpanner(object):

    def __init__(self):
        self.val = []
        self.span = []
        
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        cnt = 1
        idx = len(self.val) - 1
        while idx >= 0:
            if self.val[idx] > price:
                break
            else:
                span = self.span[idx]
                cnt += span
                idx -= span

        self.val.append(price)
        self.span.append(cnt)
        
        return cnt
        
# Stack version
    def stack__init__(self):
        self.stack = []

    def stacknext(self, price):
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == "__main__":
    S = StockSpanner()
    para = [31, 41, 48, 59, 79]
    for p in para:
        print S.next(p)
