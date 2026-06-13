# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        lh = self.height(root.left)
        rh = self.height(root.right)

        curr = abs(lh-rh) <= 1

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        return curr and left and right

    def height(self, node):

        if node is None:
            return 0

        left = self.height(node.left)
        right = self.height(node.right)

        return 1 + max(left,right)

                
            

    


            
        
        