import heapq

class KthLargest:
    k = 0
    heap = []

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
