import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = Counter(nums)
        most_frequent = []

        for item in frequency_count:
            heapq.heappush_max(most_frequent, (frequency_count[item], item))

        res = []
        while k > 0:
            _ , k_most_frequent = heapq.heappop_max(most_frequent)
            res.append(k_most_frequent)
            k -= 1

        return res