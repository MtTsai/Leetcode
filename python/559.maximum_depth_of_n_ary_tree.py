"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        
        self.maxdepth = 0
        def dfs(ptr, depth):
            if ptr:
                self.maxdepth = max(self.maxdepth, depth)

                for child in ptr.children:
                    dfs(child, depth + 1)
                                    
        dfs(root, 1)
        return self.maxdepth
