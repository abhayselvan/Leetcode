class Solution:
    def isHappy(self, n: int) -> bool:
        
        nums = set([n])
        
        while True:
            
            new = 0
            
            while n:
                new += (n % 10) ** 2
                n //= 10
            
            if new == 1:
                return True
            elif new in nums:
                return False
            else:
                nums.add(new)
            
            n = new