class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = []
        inserted = False

        for interval in intervals:
            if inserted:
                newIntervals.append(interval)
            # If the new interval is completely before the current interval,
            # and the intervals are sorted, by our logic, this means that we've
            # visited all intervals prior. So we must insert the new interval
            # immediately before the current interval
            elif newInterval[1] < interval[0]:
                newIntervals.append(newInterval)
                newIntervals.append(interval)
                inserted = True

            # If the new interval is completely after the current interval,
            # it means that we've not yet found our spot. So we simply append
            # the current interval and move on
            elif interval[1] < newInterval[0]:
                newIntervals.append(interval)

            # If the new interval has some sort of intersection with the current
            # interval, we need to merge them. We do that by getting the minimum
            # and the maximum between each, and merging them. That is because we
            # could have these scenarios:
            #
            # old => 2 ===== 4      | 2 ======== 5 |    3 == 4
            # new =>     3 ===== 5  |    3 == 4    | 2 ======== 5
            #
            # We must not yet add the merged interval, because it could merge with
            # other intervals further down the line
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        # Since we only add the new interval when it is completely before the
        # current one, we might not have added it yet. This would be the case 
        # where it's end is after the last old interval ends. Therefore, we must
        # add it after the end.
        if not inserted:
            newIntervals.append(newInterval)

        return newIntervals