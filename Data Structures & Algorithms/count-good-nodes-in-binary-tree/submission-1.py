# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, gval):
            if not node:
                return 0
            res= 1 if node.val >= gval else 0
            gval=max(gval, node.val)
            res += dfs(node.left, gval)
            res += dfs(node.right, gval)
            return res
        return dfs(root, root.val)