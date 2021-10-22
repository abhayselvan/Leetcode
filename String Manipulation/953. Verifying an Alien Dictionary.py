class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
                   
        def compare(first, second, order):

            for x, y in zip(first, second):
                if order.index(x) < order.index(y):
                    return True
                elif order.index(x) > order.index(y):
                    return False
            
            return len(first) <= len(second)
        
        
        for i in range(1,len(words)):
            if not compare(words[i-1], words[i], order):
                return False
        return True