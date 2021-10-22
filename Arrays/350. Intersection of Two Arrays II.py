class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        counter = Counter(nums1) & Counter(nums2)   
        return list(counter.elements())
            