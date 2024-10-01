# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum1, sum2 = 0, 0
        n1, n2 = 1, 1
        res = ListNode()

        while l1:
            d = l1.val
            sum1 = sum1 + (n1 * d)
            n1 = n1 * 10
            l1 = l1.next

        while l2:
            d = l2.val
            sum2 = sum2 + (n2 * d)
            n2 = n2 * 10
            l2 = l2.next

        total_sum = sum1 + sum2

        head = None
        current = None

        if total_sum == 0:
            head = ListNode(0)
            return head

        while total_sum > 0:
            d = total_sum % 10
            new_node = ListNode(d)
            if head is None:  # If it's the first node, set it as the head
                head = new_node
                current = head
            else:  # Otherwise, link it to the previous node
                current.next = new_node
                current = new_node
            total_sum = total_sum // 10
            
        
        
        return head

