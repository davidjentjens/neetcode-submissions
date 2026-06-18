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
            # If the current interval starts after the last interval ended, we can reuse a room
            # That means we pop the latest time from the heap, and push in the current interval
            if latest_end_time_heap and interval.start >= latest_end_time_heap[0]:
                heapq.heappop(latest_end_time_heap)
            # In either case, we need to push in a room:
            # Case A: Interval start time is equal or after minimum latest end time. We need to pop,
            # and then push in the current interval
            # Case B: Interval start time is before minimum latest end time. This means we need to
            # open up a new room, so we pop before we push.
            heapq.heappush(latest_end_time_heap, interval.end)

        return len(latest_end_time_heap)