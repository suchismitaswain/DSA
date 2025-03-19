def binarySearch(nums, target, searchFirst):

    (left, right) = (0, len(nums) - 1)

    result = -1

    while left <= right:

        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid
 
            if searchFirst:
                right = mid - 1
            
            else:
                left = mid + 1
 
        elif target < nums[mid]:
            right = mid - 1
        
        else:
            left = mid + 1
 
    
    return result
 
 
if __name__ == '__main__':
 
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    target = 5
 
    first = binarySearch(nums, target, True)        
    last = binarySearch(nums, target, False)        
 
    count = last - first + 1
 
    if first != -1:
        print(f'Element {target} occurs {count} times')
    else:
        print('Element found not in the list')
 

