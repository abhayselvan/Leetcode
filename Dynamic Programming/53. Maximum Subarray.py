class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum = max_sum = nums[0]
        
        for i in range(1, len(nums)):
            sum = max(sum + nums[i], nums[i])
            max_sum = max(sum, max_sum)
            
        return max_sum