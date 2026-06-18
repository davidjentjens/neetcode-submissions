class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        inserted = False
        for interval in intervals:
            if inserted or interval[1] < newInterval[0]:
                new_intervals.append(interval)
            elif newInterval[1] < interval[0]:
                new_intervals.append(newInterval)
                new_intervals.append(interval)
                inserted = True
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not inserted:
            new_intervals.append(newInterval)
        return new_intervals