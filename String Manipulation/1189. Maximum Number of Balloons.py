from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        counter = Counter(text)
        min_count = float('inf')
         
        for ch in 'balloon':
            if ch not in counter:
                return 0
            min_count = min(min_count, counter[ch] // 'balloon'.count(ch))
            
        return min_count