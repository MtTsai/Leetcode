# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.is_balanced = True
        def dfs(ptr, depth):
            l, r = depth, depth
            if ptr.left:
                l = dfs(ptr.left, depth + 1)
            if ptr.right:
                r = dfs(ptr.right, depth + 1)
            if self.is_balanced:
                dist = l - r
                self.is_balanced = False if dist > 1 or dist < -1 else True
            return max(l, r)
                
        dfs(root, 0)
        return self.is_balanced
