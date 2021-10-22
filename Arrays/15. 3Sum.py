class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans, check_duplicates, seen = set(), set(), {}
        
        for i, num1 in enumerate(nums):
            
            if num1 not in check_duplicates:
                check_duplicates.add(num1)
            
                for j, num2 in enumerate(nums[i+1:]):

                    target = -num1 - num2

                    if target in seen and seen[target] == i:
                        ans.add(tuple(sorted((target, num1, num2))))
                    seen[num2] = i
                
        return ans