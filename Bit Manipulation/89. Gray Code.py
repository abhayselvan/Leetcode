class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        ans = [0]
        for i in range(n):
            ans += [x|(1<<i) for x in ans[::-1]]
        return ans