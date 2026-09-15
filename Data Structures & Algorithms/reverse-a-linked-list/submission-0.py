# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()

        while head:
            stack.append(head.val)
            head = head.next
        
        if len(stack) == 0:
            return None
        res = ListNode()
        h = res
        while len(stack) != 0:
            res.val = stack.pop()
            if len(stack) == 0:
                break
            res.next = ListNode()
            res = res.next
        
        return h