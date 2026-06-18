class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        merged_lists = []

        for interval in sorted_intervals:
            start, end = interval
            if merged_lists and merged_lists[-1][-1] >= start:
                merged_lists[-1][1] = max(merged_lists[-1][1], end)
            else:
                merged_lists.append([start, end])

        return merged_lists