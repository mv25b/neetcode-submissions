# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        #reverses a Linked list, will reverse rhs
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        dummy = head
        #count number of nodes
        while dummy:
            count+=1
            dummy = dummy.next
        
        #finds midpoint, move right pointer to it 
        mid = (count + 1) // 2
        left, right = head, head
        for i in range(mid-1):
            right = right.next
        
        tmp = right.next
        right.next = None
        right = tmp

        #reverses right list
        right = self.reverseList(right)

        #merges lists together 
        while right:
            nextLeft, nextRight = left.next, right.next

            left.next = right
            right.next = nextLeft

            left,right = nextLeft, nextRight

        return None
        