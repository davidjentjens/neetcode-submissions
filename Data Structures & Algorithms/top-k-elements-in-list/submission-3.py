class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        frequencies = Counter(nums)
        bucket = [[] for i in range(n + 1)]

        for num, freq in frequencies.items():
            bucket[freq].append(num)

        k_most = []

        for i in range(n, -1, -1):
            for bucket_item in bucket[i]:
                k_most.append(bucket_item)
                if len(k_most) == k:
                    return k_most

        return k_most
        