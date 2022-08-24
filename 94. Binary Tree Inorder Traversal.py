# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, root, result):
        if root:
            self.helper(root.left,result)
            result.append(root.val)
            self.helper(root.right,result)
    def inorderTraversal(self, root):
     
        result = []
        self.helper(root,result)
        return result
  