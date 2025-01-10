class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        oper = 0
        pb = nums[-1]

        for num in reversed(nums[:-1]):
            times = (num + pb - 1) // pb
            oper += times - 1
            pb = num // times
        return oper
        