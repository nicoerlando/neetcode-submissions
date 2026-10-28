# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return False

            if root and subRoot and root.val == subRoot.val and self.isSameTree(root, subRoot):
                return True
        
            return dfs(root.left) or dfs(root.right)
        
        if not subRoot:
            return True

        return dfs(root)

    def isSameTree(self, p, q):

        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        