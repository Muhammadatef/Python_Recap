
##Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.


from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = " ".join(strs)  # Join the list into a single string with spaces
        self.decode(s)      # Call to decode (not used further)
        return s            # Return the encoded string

    def decode(self, s: str) -> List[str]:
        result = s.split(' ')  # Split the string back into a list
        return list(result)     # Return the list

# Example usage:
solution = Solution()

# Example 1
input_data_1 = ["hello", "world", "test"]
encoded_1 = solution.encode(input_data_1)
print(f"Encoded 1: {encoded_1}")  # Output: "hello world test"
decoded_1 = solution.decode(encoded_1)
print(f"Decoded 1: {decoded_1}")  # Output: ['hello', 'world', 'test']

# Example 2
input_data_2 = ["this", "is", "a", "test"]
encoded_2 = solution.encode(input_data_2)
print(f"Encoded 2: {encoded_2}")  # Output: "this is a test"
decoded_2 = solution.decode(encoded_2)
print(f"Decoded 2: {decoded_2}")  # Output: ['this', 'is', 'a', 'test']


