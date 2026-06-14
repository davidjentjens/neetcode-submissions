class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l, r = 0, k
        max_window = []
        max_heap = [(val, i) for i, val in enumerate(nums[l:r-1])]
        heapq.heapify_max(max_heap)
        
        while r <= n:
            heapq.heappush_max(max_heap, (nums[r-1], r-1))

            max_val, max_pos = max_heap[0]
            while max_pos < l:
                heapq.heappop_max(max_heap)
                max_val, max_pos = max_heap[0]

            max_window.append(max_heap[0][0])
            l += 1
            r += 1

        return max_window