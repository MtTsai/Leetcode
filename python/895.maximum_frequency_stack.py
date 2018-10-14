class FreqStack(object):
    
    def __init__(self):
        self.stack = [[0]]
        self.freq = {}
        
        self.maxf = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        freq = self.freq[x] = self.freq.get(x, 0) + 1
        
        if (len(self.stack) - 1) < freq:
            self.stack.append([])
            
        self.stack[freq].append(x)
        
        self.maxf = max(self.maxf, freq)
        
    def pop(self):
        """
        :rtype: int
        """
        v = self.stack[self.maxf].pop()
        while len(self.stack[self.maxf]) == 0:
            self.maxf -= 1
        
        self.freq[v] -= 1
        
        return v
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
