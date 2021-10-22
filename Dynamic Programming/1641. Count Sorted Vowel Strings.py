class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        self.memo = {}
        return self.dfs(n, 5)
    
    def dfs(self, n, k):

        if n == 1 or k == 1:
            return k

        if (n, k) not in self.memo:
            self.memo[n, k] = sum(self.dfs(n-1, k) for k in range(1, k+1))

        return self.memo[n, k]