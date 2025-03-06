from typing import List

def dominantIndex(self, nums: List[int]) -> int:
        a=max(nums)
        for i in nums:
            if i!=a and a<i*2:
                return -1
        return nums.index(a)