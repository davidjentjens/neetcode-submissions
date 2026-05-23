class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        sorted_frequency = sorted(frequency.items(), key=lambda item: -item[1])
        return [item[0] for item in sorted_frequency[:k]]
