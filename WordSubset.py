from typing import Counter, List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq = Counter()
        for b in words2:
            freq |= Counter(b)
        
        ans = []
        for a in words1:
            if not (freq - Counter(a)):
                ans.append(a)
        
        return ans
        