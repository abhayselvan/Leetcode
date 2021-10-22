class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        incr = decr = False
        
        for i in range(1, len(arr)):
            
            if arr[i] > arr[i-1] and not decr:
                incr = True
            
            elif arr[i] < arr[i-1] and incr:
                decr = True
                
            else:
                return False
            
        return incr and decr