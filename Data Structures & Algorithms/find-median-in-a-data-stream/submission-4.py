class MedianFinder:
    def __init__(self):
        self.max_heap_left = []
        self.min_heap_right = []
        self.median = None

    def addNum(self, num: int) -> None:
        if self.median == None:
            self.median = num
            return
        if isinstance(self.median, int):
            if len(self.max_heap_left) and num < self.max_heap_left[0]:
                new_left_elem = heapq._heappop_max(self.max_heap_left)
                heapq.heappush_max(self.max_heap_left, num)
                self.median = (new_left_elem, self.median)
                return
            elif len(self.min_heap_right) and num > self.min_heap_right[0]:
                new_right_elem = heapq.heappop(self.min_heap_right)
                heapq.heappush(self.min_heap_right, num)
                self.median = (self.median, new_right_elem)
                return
            self.median = (num, self.median) if num < self.median else (self.median, num)
            return
        else:
            sorted_trio = sorted([self.median[0], self.median[1], num])
            heapq.heappush_max(self.max_heap_left, sorted_trio[0])
            self.median = sorted_trio[1]
            heapq.heappush(self.min_heap_right, sorted_trio[2])

    def findMedian(self) -> float:
        if self.median == None: 
            return None
        
        if isinstance(self.median, tuple):
            return (self.median[0] + self.median[1]) / 2

        return self.median

        