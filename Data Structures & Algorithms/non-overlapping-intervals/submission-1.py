import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        prev_interval = None
        substitutions = 0

        for interval in sorted_intervals:
            if prev_interval and interval[0] < prev_interval[1]:
                substitutions += 1
                if prev_interval[1] <= interval[1]:
                    continue
            prev_interval = interval

        return substitutions
