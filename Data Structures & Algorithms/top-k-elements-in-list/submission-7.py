import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in frequency_count.items():
            buckets[freq].append(num)
        
        counter = len(buckets) - 1
        res = []
        while k > 0:
            for num in buckets[counter]:
                res.append(num)
                k -= 1
                if k == 0:
                    break
            counter -= 1
            
        return res