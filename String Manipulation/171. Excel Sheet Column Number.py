class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        ALPHABET_SIZE = 26
        base = ord('A') - 1
        
        num = 0
        
        for index, letter in enumerate(reversed(columnTitle)):
            num += (ord(letter) - base) * (ALPHABET_SIZE**index)
            
        return num