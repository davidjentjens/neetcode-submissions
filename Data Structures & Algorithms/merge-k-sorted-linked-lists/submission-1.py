# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = ListNode(0)
        node = merged_list

        heap = []
        for i, sublist in enumerate(lists):
            if sublist:
                heapq.heappush(heap, (sublist.val, i, sublist))

        while len(heap) > 0:
            # Pop smallest node from the heap
            smallest_node_val, i, smallest_node = heapq.heappop(heap)

            node.next = smallest_node # Add smallest node to merged list
            node = node.next # Move merged list forward

            # Cleanup -> If it exists, push the next list element back into the heap
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, i, smallest_node.next))

        return merged_list.next

            