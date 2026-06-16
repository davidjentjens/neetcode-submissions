class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        valid_triplets = []

        for i in range(n):
            l, r = i+1, n - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    valid_triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1

        return valid_triplets