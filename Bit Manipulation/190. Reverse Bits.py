class Solution:
    def reverseBits(self, n: int) -> int:
        
        m = 0
        pos = 31
        
        while n:
            
            bit = n & 1
            m += bit << pos
            n = n >> 1
            pos -= 1    
            
        return m