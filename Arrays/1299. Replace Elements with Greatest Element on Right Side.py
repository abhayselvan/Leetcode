class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_element = -1
        
        for i in reversed(range(len(arr))):
            
            arr[i], max_element = max_element, max(arr[i], max_element)
            
        return arr