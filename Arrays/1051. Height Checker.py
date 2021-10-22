class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)
        not_matching = 0
        
        for x, y in zip(heights, expected):
            if x != y:
                not_matching += 1
                
        return not_matching
            