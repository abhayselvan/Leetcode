from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = Counter(s)
        
        for key in d:
            if d[key] == 1:
                return s.find(key)
            
        return -1