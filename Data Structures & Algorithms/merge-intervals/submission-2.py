class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])        
        merged_intervals = []
        new_interval = sorted_intervals[0]

        for interval in sorted_intervals:
            if new_interval[1] < interval[0]:
                merged_intervals.append(new_interval)
                new_interval = interval
                continue
            
            new_interval = [new_interval[0], max(new_interval[1], interval[1])]
        merged_intervals.append(new_interval)

        return merged_intervals
            
            

