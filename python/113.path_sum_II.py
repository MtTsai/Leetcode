# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        def traverse(node, curr, curr_sum):
            if node:
                curr.append(node.val)
                if not node.left and not node.right and curr_sum + node.val == sum:
                    ans.append(list(curr))
                traverse(node.left, curr, curr_sum + node.val)
                traverse(node.right, curr, curr_sum + node.val)
                curr.pop()

        traverse(root, collections.deque([]), 0)
        return ans
