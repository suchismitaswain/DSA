def hasQuadruplet(nums, n, target, count):

    if target == 0 and count == 4:
        return True

    if count > 4 or n == 0:
        return False

    return hasQuadruplet(nums, n - 1, target - nums[n - 1], count + 1) or\
        hasQuadruplet(nums, n - 1, target, count)
 
 
if __name__ == '__main__':
 
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 20
 
    if hasQuadruplet(nums, len(nums), target, 0):
        print('Quadruplet exists')
    else:
        print('Quadruplet doesn\'t exist')