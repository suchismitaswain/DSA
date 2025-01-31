import math
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        first = second = third = -math.inf
        for num in nums:
            if num > first and num > second and num > third:
                first = num
            elif num > second and num > third:
                if first != num:
                    second = num
            elif num > third:
                if second != num:
                    return num
        
        return first
        