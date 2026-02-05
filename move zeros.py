class Solution:
    def moveZeroes(self, nums):
        pos = 0  # position for next non-zero

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Fill remaining positions with zero
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
