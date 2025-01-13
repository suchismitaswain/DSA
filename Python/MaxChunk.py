from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count =0
        max_so = -1
        for i, val in enumerate(arr):
            max_so = max(max_so, val)
            if max_so <= i:
                count+=1
        return count