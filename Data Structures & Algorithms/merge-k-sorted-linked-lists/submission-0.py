# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = ListNode(0)
        node = merged_list
        n = len(lists)

        while n > 0:
            smallest_node_val, smallest_node_index = float('inf'), 0
            for i, sublist in enumerate(lists):
                if sublist and sublist.val < smallest_node_val:
                    smallest_node_val = sublist.val
                    smallest_node_index = i

            node.next = lists[smallest_node_index] # Add smallest node to merged list
            node = node.next # Move merged list forward

            # Cleanup -> Remove node from the previous list
            if lists[smallest_node_index].next == None:
                n -= 1 # The list is empty, so we may decrease n by 1
                lists[smallest_node_index] = None
            else:
                lists[smallest_node_index] = lists[smallest_node_index].next # Remove smallest node from list

        return merged_list.next

            