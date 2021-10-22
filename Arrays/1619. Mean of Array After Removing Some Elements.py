class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        arr.sort()
        n = len(arr)
        p5 = n * 5 // 100 
        base = p5
        new_arr = arr[p5:n-p5]
        
        return sum(new_arr) / len(new_arr)