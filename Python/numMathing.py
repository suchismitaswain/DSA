from typing import List

def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_substring(substring):
            pos = -1
            for char in substring:
                pos = s.find(char, pos+1)
                if pos == -1: return False
            return True
        return sum(map(is_substring, words))