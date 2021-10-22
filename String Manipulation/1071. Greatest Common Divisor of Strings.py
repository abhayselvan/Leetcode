class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str2) > len(str1):
            str1, str2 = str2, str1
         
        gcd = str2
        
        while gcd:
            
            n = len(gcd)
            s1, s2 = str1, str2
            
            while s1:
                if s1.startswith(gcd):
                    s1 = s1[n:]
                else:
                    break
                    
            while s2:
                if s2.startswith(gcd):
                    s2 = s2[n:]
                else:
                    break
            
            if not s1 and not s2:
                return gcd
            
            gcd = gcd[:-1]
                
        return ""
            
                    
            