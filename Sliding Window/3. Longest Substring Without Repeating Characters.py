class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substrings = {}
        start = count = 0
        
        for index, ch in enumerate(s):
            if ch in substrings:
                start = max(substrings[ch], start)
                
            count = max(count, index - start + 1)
            substrings[ch] = index + 1
                
        return count