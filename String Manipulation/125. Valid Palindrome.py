class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = []
        
        for ch in s:
            if ch.isalnum():
                word.append(ch)
                
        word = "".join(word).lower()
        
        return word == word[::-1]