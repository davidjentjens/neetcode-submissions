class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        sorted_frequency = sorted(frequency.items(), key=lambda item: -item[1])
        k_most = sorted_frequency[:k]

        return list(map(lambda item: item[0], k_most))
