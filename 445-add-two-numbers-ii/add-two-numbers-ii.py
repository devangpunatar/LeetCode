# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, sum2 = 0, 0
        while l1:
            d = l1.val
            sum1 = sum1 * 10 + d
            l1 = l1.next
        while l2:
            d = l2.val
            sum2 = sum2 * 10 + d
            l2 = l2.next
        
        total = str(sum1 + sum2)
        if total == "0":
            head = ListNode(0)
            return head

        head, curr = None, None
        for char in total:
            newNode = ListNode(int(char))
            if head == None: 
                head = newNode
                curr = head
            else:
                curr.next = newNode
                curr = newNode
        
        return head