# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        def traverse(node, curr_sum):
            if not node:
                return False
            curr_sum += node.val
            if (curr_sum == sum and not node.left and not node.right) or traverse(node.left, curr_sum) or traverse(node.right, curr_sum):
                return True
            return False
                
        
        return traverse(root, 0)
