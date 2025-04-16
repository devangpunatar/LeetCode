# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashSet = set()
        currA = headA
        currB = headB

        while currA:
            hashSet.add(currA)
            currA = currA.next
        
        while currB:
            if currB in hashSet:
                return currB
            currB = currB.next
        
        return None