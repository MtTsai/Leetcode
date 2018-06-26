# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.mode = {}
        self.max = 0
        
        def dfs(trie):
            if trie:
                v = trie.val
                self.mode[v] = self.mode.get(v, 0) + 1
                self.max = max(self.max, self.mode[v])
                dfs(trie.left)
                dfs(trie.right)
        dfs(root)
        return [v for v in self.mode if self.mode[v] == self.max]
