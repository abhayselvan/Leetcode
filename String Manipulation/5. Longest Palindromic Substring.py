class Solution:
    
    
    
    def longestPalindrome(self, s: str) -> str:
        
        ans = ""
        
        for i in range(len(s)):
            
            palindrome1 = self.check_palindrome(s, i, i)
            palindrome2 = self.check_palindrome(s, i, i+1)
            
            ans = max(ans, palindrome1, palindrome2, key=len)
            
        return ans
            
        
    def check_palindrome(self, s, start, end):
        
        while start >= 0 and end < len(s) and s[start] == s[end]: 
            
            start -= 1
            end += 1
                
        return s[start+1:end]