from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        a = [1] * n
        prev = [-1] * n
        max_len, max_index = 0, -1

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and a[j] + 1 > a[i]:
                    
                    a[i] = a[j] + 1
                    prev[i] = j

            if a[i] > max_len:
                max_len = a[i]
                max_index = i

        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]

        return result