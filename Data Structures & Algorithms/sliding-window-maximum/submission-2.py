import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_heap = []
        res = []

        for right in range(n):
            heapq.heappush_max(max_heap, (nums[right], right))
            if right >= k - 1:
                while max_heap[0][1] <= right - k: # While the biggest element is out of the window
                    heapq.heappop_max(max_heap)
                res.append(max_heap[0][0])

        return res
            