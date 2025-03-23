# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        Let's say we have 1 -> 2 -> 3, if we were to reverse it to 
        1 -> 3 -> 2, we would have to add the group of 3 -> 2, somewhere
        and we would add it to groupPrev
        """
        dummy = ListNode(0, head)
        groupPrev = dummy 

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reversing the group
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth 
            groupPrev = temp  

        return dummy.next        

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
