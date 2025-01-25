from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0

        res = []

        n1 = len(nums1)
        n2 = len(nums2)

        while p1 < n1 and p2 < n2:
            if nums1[p1][0] < nums2[p2][0]:
                res.append(nums1[p1])
                p1 += 1
            
            elif nums2[p2][0] < nums1[p1][0]:
                res.append(nums2[p2])
                p2 += 1
            
            else:
                res.append([nums1[p1][0], nums1[p1][1] + nums2[p2][1]])
                p1 += 1
                p2 += 1
        while p1 < n1:
            res.append(nums1[p1])
            p1 += 1

        while p2 < n2:
            res.append(nums2[p2])
            p2 += 1

        return res
        