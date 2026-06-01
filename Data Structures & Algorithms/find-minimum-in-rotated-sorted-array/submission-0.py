class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while (l < r):
            mid = (l + r) // 2

            if nums[mid] > nums[r]: # Left side is sorted, => smallest element is not here
                l = mid + 1
            else: # Right side is sorted => smallest element is not here
                r = mid

        return nums[l]
