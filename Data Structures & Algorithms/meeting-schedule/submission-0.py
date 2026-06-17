"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)

        # 0 -------------- 6
        #   1 - 2
        #.        3 - 4

        if len(sorted_intervals) <= 1:
            return True

        for i in range(1, len(sorted_intervals)):
            print(sorted_intervals[i-1].start, sorted_intervals[i-1].end, sorted_intervals[i].start, sorted_intervals[i].end)
            if sorted_intervals[i-1].end > sorted_intervals[i].start:
                return False
            print('\n')

        return True
