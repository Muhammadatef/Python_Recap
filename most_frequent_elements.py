class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        
        # Count the frequency of each element
        for i in nums:
            key = i
            if i not in dic:
                dic[i] = 0
            dic[key] = dic[key] + 1
        
        # Sort the dictionary by frequency in descending order
        sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the top k frequent elements
        result = [item[0] for item in sorted_dic[:k]]
        
        return result

s = Solution()
print(s.topKFrequent([1,1,1,1,2,2,3,],2))
