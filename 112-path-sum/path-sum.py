# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [[root, targetSum]]

        while stack:
            node, total = stack.pop()
            if node:
                total -= node.val
                if node.left is None and node.right is None and total == 0:
                    return True
                stack.append([node.left, total])
                stack.append([node.right, total])

        return False