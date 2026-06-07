class MedianFinder:
    def __init__(self):
        self.max_heap_left = []
        self.min_heap_right = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max_heap_left, num)
        if self.min_heap_right and self.max_heap_left[0] > self.min_heap_right[0]:
            heapq.heappush(self.min_heap_right, heapq.heappop_max(self.max_heap_left))
        if len(self.max_heap_left) > len(self.min_heap_right) + 1:
            heapq.heappush(self.min_heap_right, heapq.heappop_max(self.max_heap_left))
        elif len(self.min_heap_right) > len(self.max_heap_left):
            heapq.heappush_max(self.max_heap_left, heapq.heappop(self.min_heap_right))

    def findMedian(self) -> float:
        if len(self.max_heap_left) > len(self.min_heap_right):
            return self.max_heap_left[0]
        return (self.max_heap_left[0] + self.min_heap_right[0]) / 2
