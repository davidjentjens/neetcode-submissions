# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = 0
        node = head
        while node != None:
            node = node.next
            end += 1
        target = end - n

        if target == 0:
            return head.next

        node = head
        i = 0
        while i < target-1:
            node = node.next
            i += 1
        
        if node.next != None:
            node.next = node.next.next

        return head