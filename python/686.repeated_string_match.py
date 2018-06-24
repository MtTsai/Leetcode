# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        def max_tree(arrays):
            if not arrays:
                return None
            
            maxid, maxval = 0, arrays[0]
            for idx, value in enumerate(arrays):
                if value > maxval:
                    maxid, maxval = idx, value
                    
            trie = TreeNode(maxval)
            trie.left = max_tree(arrays[:maxid])
            trie.right = max_tree(arrays[maxid + 1:])

            return trie

        return max_tree(nums)
