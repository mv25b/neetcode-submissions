# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge case - no linked list/just one node
        if not head:
            return None

        if not head.next:
            return head

        slow = head
        fast = head.next
        head.next = None

        while fast:
            tmp = fast.next
            fast.next = slow


            slow = fast
            fast= tmp
        
        return slow