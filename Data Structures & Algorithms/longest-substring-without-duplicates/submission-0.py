class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        left = 0  
        for right in range(len(s)):
            char = s[right]
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            current_window_length = right - left + 1
            max_length = max(max_length, current_window_length)
            
        return max_length
   
                