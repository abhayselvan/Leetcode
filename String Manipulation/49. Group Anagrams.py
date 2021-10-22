from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_sets = defaultdict(list)
        
        for word in strs:
            anagram_sets[tuple(sorted(word))].append(word)
            
        return anagram_sets.values()
            