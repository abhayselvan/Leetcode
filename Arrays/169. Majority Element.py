class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         
        target = (len(nums) // 2) + 1
        
        d = {}
        
        for num in nums:
            
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
            if d[num] >= target:
                return num
            
            
                
        