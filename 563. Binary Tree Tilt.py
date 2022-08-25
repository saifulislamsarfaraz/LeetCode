# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int"""
        self.res = 0
        def recursive(root):
            if not root: return 0
            left = recursive(root.left)
            right = recursive(root.right)
            self.res += abs(left-right)
            return root.val + left + right
    
        recursive(root)
        return self.res

        
        