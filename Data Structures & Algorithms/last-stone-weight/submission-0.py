import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x == y:
                continue
            else:
                new_stone = max(x,y) - min(x,y)
            heapq.heappush_max(stones, new_stone)

        print(stones)

        return 0 if len(stones) == 0 else stones[0]