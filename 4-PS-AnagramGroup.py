##https://neetcode.io/problems/anagram-groups
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Initialize a dictionary to map sorted string keys to their corresponding anagrams
        anagram_map = {}
        
        # Iterate through each string in the input list
        for s in strs:
            # Sort the characters in the string and join them to form a key
            # This key will be the same for all anagrams (e.g., 'act' and 'cat' will both give 'act')
            key = ''.join(sorted(s))
            
            # If the key is not already in the map, initialize an empty list for it
            if key not in anagram_map:
                anagram_map[key] = []
            
            # Append the original string to the list corresponding to its sorted key
            anagram_map[key].append(s)
        
        # Return a list of the values in the anagram_map, which are lists of grouped anagrams
        return list(anagram_map.values())

# Create an instance of the Solution class
s = Solution()

# Call the groupAnagrams method with the given list and store the result
result = s.groupAnagrams(strs = ["act", "pots", "tops", "cat", "stop", "hat"])

# Print the grouped anagrams
print(result)
