class Solution:
    def numDecodings(self, s: str) -> int:
        
        self.memo = {}
        
        return self.checkString(s)
         
    def checkString(self, s):
        
        if not s:
            return 1
        
        if s[0] == "0":
            return 0

        if s in self.memo:
            return self.memo[s]
        
        res = 0
        
        res += self.checkString(s[1:])
        
        if 10 <= int(s[:2]) <= 26:
            res += self.checkString(s[2:])
            
        self.memo[s] = res
        return res
            