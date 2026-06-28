class Solution:
    def isValid(self, k: int, piles: List[int], h: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
            if hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, max(piles)

        while min_k <= max_k:
            k = (min_k + max_k) // 2
            if self.isValid(k, piles, h):
                max_k = k-1
            else:
                min_k = k+1

        return min_k


        