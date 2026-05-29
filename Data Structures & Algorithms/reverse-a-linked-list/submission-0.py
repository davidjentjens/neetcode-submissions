# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        next_node = None

        while head != None:
            # Save reference to the "next" element, which will point here
            next_node = head.next
            # Pointing here to the previous node
            head.next = previous_node
            # Pointing the previous node to the current node
            previous_node = head
            # Advancing to the next item
            head = next_node

        return previous_node