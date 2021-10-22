class Solution:
    def isValid(self, s: str) -> bool:
        
        dic = {
            '(':')',
            '[':']',
            '{':'}'
        }
        
        stack = []
        
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif not stack:
                return False
            elif ch == dic[stack[-1]]:
                stack.pop()
            else:
                return False
                
        return not stack