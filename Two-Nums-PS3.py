##Two-Nums
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indecies=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    indecies.append(i)
                    indecies.append(j)
        return indecies

s=Solution()
print(s.twoSum(nums=[3,4,5,6,7,8,9],target=17))