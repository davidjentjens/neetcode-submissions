# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head

        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # Start second half without the first element (middle element)
        second_half = slow.next
        # Set cutoff point to None, to prevent a cycle
        slow.next = None
        # Get head of reversed second half of the list
        reversed_half = self.reverseList(second_half)

        # Iterate through list, adding the reversed nodes in between
        node = head
        while node and reversed_half:
            node_next = node.next # Save next ordered node
            reversed_half_next = reversed_half.next # Save next reversed node

            reversed_half.next = node_next # Connect reversed node to next ordered node
            node.next = reversed_half # Connect node to unordered node

            node = node_next # Move to the next ordered node
            reversed_half = reversed_half_next # Move to the next unordered node        
