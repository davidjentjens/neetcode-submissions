class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        valid_triplets = set()

        for i in range(n):
            l, r = 0, n - 1

            while l < r:
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplet = sorted([nums[i], nums[l], nums[r]])
                    valid_triplets.add((triplet[0], triplet[1], triplet[2]))
                    l += 1

        return list(valid_triplets)