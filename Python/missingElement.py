def findSmallestMissing(nums, left=None, right=None):
 
    if left is None and right is None:
        (left, right) = (0, len(nums) - 1)
 
    if left > right:
        return left
 
    mid = left + (right - left) // 2
 
    if nums[mid] == mid:
        return findSmallestMissing(nums, mid + 1, right)
 
    else:
        return findSmallestMissing(nums, left, mid - 1)
 
 
if __name__ == '__main__':
 
    nums = [0, 1, 2, 3, 4, 5, 6]
 
    print('The smallest missing element is', findSmallestMissing(nums))