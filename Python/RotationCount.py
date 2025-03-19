def findRotationCount(nums):

    (left, right) = (0, len(nums) - 1)
 
    while left <= right:
 
        if nums[left] <= nums[right]:
            return left
 
        mid = (left + right) // 2
        next = (mid + 1) % len(nums)
        prev = (mid - 1 + len(nums)) % len(nums)
 
        if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
            return mid
 
        elif nums[mid] <= nums[right]:
            right = mid - 1
 
        elif nums[mid] >= nums[left]:
            left = mid + 1

    return -1
 
 
if __name__ == '__main__':
 
    nums = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
    print(f'The list is rotated {findRotationCount(nums)} times')
 