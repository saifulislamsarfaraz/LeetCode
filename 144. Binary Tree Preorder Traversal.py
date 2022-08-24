# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
    def helper(self, root, result):
        if root:
            result.append(root.val)
            self.helper(root.left,result)
            
            self.helper(root.right,result)
    def preorderTraversal(self, root):
        result = []
        self.helper(root,result)
        return result