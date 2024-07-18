# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        resultP = []
        resultQ = []
        def pre_order_traversal(p, resultP):
            if p:
                resultP.append(p.val)
                pre_order_traversal(p.left, resultP)
                pre_order_traversal(p.right, resultP)
            else:
                resultP.append(None)

        def pre_order_traversal(q, resultQ):
            if q:
                resultQ.append(q.val)
                pre_order_traversal(q.left, resultQ)
                pre_order_traversal(q.right, resultQ)
            else:
                resultQ.append(None)
                
        pre_order_traversal(p, resultP)
        pre_order_traversal(q, resultQ)

        if resultP == resultQ:
            return True
        else:
            return False