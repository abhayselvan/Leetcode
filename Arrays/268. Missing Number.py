class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        actual_sum = sum(nums)
        
        expected_sum = len(nums) * (len(nums) + 1) // 2
        
        missing_number = expected_sum - actual_sum
        
        return missing_number