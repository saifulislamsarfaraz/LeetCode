# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            return TreeNode(val, left=root)
        self.addOneRowRecursive(root,val,depth,1)
        return root
    
    def addOneRowRecursive(self, root,val, depth, level):
        if depth - 1 == level:
            leftTree = TreeNode(val,left=root.left)
            rightTree = TreeNode(val,right=root.right)
            
            root.left = leftTree
            root.right = rightTree
            return
        
        if root.left:
            self.addOneRowRecursive(root.left,val,depth,level+1)
        if root.right:
            self.addOneRowRecursive(root.right,val,depth,level+1)
            
