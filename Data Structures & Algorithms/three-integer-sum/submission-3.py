class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = set()

        for k in range(n):
            l, r = k+1, n-1
            if nums[k] > 0:
                break
            while (l < r):
                trio_sum = nums[l] + nums[r] + nums[k]
                if trio_sum == 0:
                    result.add((nums[l], nums[r], nums[k]))
                    l += 1
                    r -= 1
                elif trio_sum < 0:
                    l += 1
                elif trio_sum > 0:
                    r -= 1

        return list(result)