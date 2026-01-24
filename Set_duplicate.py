from typing import List   # MUST be first line


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        for i in range(1, len(nums)):
            if nums[c] != nums[i]:
                c += 1
                nums[c] = nums[i]
        return c + 1

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# -------- TESTING --------
sol = Solution()

nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = sol.removeDuplicates(nums1)
print(k)
print(nums1[:k])

nums2 = [1, 2, 3, 1]
print(sol.containsDuplicate(nums2))
