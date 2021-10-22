class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        res1 = {res: index for index, res in enumerate(list1)}
        res2 = {res: index + res1[res] for index, res in enumerate(list2) if res in res1}
        
        ans = []
        best = float('inf')
        
        for key, value in res2.items():
            if value < best:
                best = value
                ans = [key]
            elif value == best:
                ans.append(key)
                
        return ans