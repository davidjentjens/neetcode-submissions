class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # If right side is sorted
            if nums[mid] <= nums[r]:
                # Check if target is within the sorted side. 
                # If not, continue the search on the unsorted side
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            # If left side is sorted
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1

        return -1