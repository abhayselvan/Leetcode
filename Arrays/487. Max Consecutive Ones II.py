class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        zeros = max_count = start = 0
           
        for i in range(len(nums)):
            
            if nums[i] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[start] == 0:
                    zeros -= 1
                start += 1          
                    
            max_count = max(max_count, i - start + 1)
                    
        return max_count