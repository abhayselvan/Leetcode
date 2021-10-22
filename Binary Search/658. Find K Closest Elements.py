class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        closest_elements = self.binary_search(arr, x, k, 0, len(arr)-1)
        
        while len(closest_elements) > k:
            if abs(closest_elements[0] - x) > abs(closest_elements[-1] - x):
                closest_elements.pop(0)
            else:
                closest_elements.pop()
                
        return closest_elements
        
        
    def binary_search(self, arr, x, k, low, high):
        
        if low >= high:
            return self.k_closest_array(arr, low, k)
        
        mid = (low + high) // 2
        
        if arr[mid] == x:
            return self.k_closest_array(arr, mid, k) 
        
        if arr[mid] < x:
            return self.binary_search(arr, x, k, mid+1, high)
            
        else:
            return self.binary_search(arr, x, k, low, mid)
            
    def k_closest_array(self, arr, mid, k):
         
        if mid == 0:
            return arr[mid:mid+k+1]
        
        if mid == len(arr) - 1:
            return arr[mid-k:mid+1]
        
        low = mid - k if mid - k > 0 else 0
        high = mid + k + 1 if mid + k + 1 < len(arr) else len(arr)
        return arr[low:mid] + arr[mid:high]
