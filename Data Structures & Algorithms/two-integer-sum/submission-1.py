class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for a in range(n):
            for b in range(a+1, n):
                if (nums[a] + nums[b] == target):
                    return [a, b]
                b += 1
            a += 1

        return None