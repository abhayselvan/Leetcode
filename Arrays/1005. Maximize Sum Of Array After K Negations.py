class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
            
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] < 0:
                if k > 0:
                    nums[i] = -nums[i]
                    k -= 1
                else:
                    break
            else:
                if k % 2 != 0:
                    if nums[i-1] and nums[i-1] < nums[i]:
                        nums[i-1] = -nums[i-1]
                    else:
                        nums[i] = -nums[i]
                break
                
        return sum(nums)