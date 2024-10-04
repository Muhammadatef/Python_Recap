class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): ##compare to the next element
                if nums[i] == nums[j]: ## compare the values not the indices (i==j)
                    return True  # return True if it finds duplicates instantly
        return False

s = Solution()
print(s.hasDuplicate([1, 2, 3, 4]))  # Output: False
print(s.hasDuplicate([1, 2, 3, 3]))  # Output: True

