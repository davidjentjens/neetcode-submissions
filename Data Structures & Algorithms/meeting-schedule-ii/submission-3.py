"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
        latest_end_time_heap = []
        
        for interval in sorted_intervals:
            if latest_end_time_heap and latest_end_time_heap[0] <= interval.start:
                heapq.heappop(latest_end_time_heap)

            heapq.heappush(latest_end_time_heap, interval.end)

        return len(latest_end_time_heap)