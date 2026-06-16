class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        valid_triplets = []

        for i in range(n):
            # We start the left pointer at i+1, because everything to the left of i has already been taken
            # into account, in previous iterations of i.
            l, r = i + 1, n - 1

            # Element i was the anchor in the previous operation. If it is a duplicate, we can skip it.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                # If the sum is smaller than 0, we need to move the left pointer to the right, so
                # as to get fewer negative/smaller numbers.
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                # The opposite goes for the right side.
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    valid_triplets.append([nums[i], nums[l], nums[r]])
                    # Here we can move both l and r at the same time, because there will be no valid
                    # combinations if we unequally shrink one of the sides.
                    l += 1
                    r -= 1
                    # We must move both l and r while their values remain equal to their previous
                    # value, to avoid duplicates.
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1

        return valid_triplets