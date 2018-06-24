class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dq = collections.deque([], capacity)
        self.vtable = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.vtable:
            self.dq.remove(key)
            self.dq.append(key)
            return self.vtable[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.vtable:
            self.dq.remove(key)
            self.dq.append(key)
        else:
            if len(self.dq) == self.dq.maxlen:
                self.vtable.pop(self.dq.popleft())
            self.dq.append(key)
            
        self.vtable[key] = value    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
