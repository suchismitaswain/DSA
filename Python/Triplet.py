def isTripletExist(nums, n, target, count):

    if count == 3 and target == 0:
        return True

    if count == 3 or n == 0 or target < 0:
        return False

    return isTripletExist(nums, n - 1, target - nums[n - 1], count + 1) or\
        isTripletExist(nums, n - 1, target, count)
 
 
if __name__ == '__main__':
 
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 6
 
    if isTripletExist(nums, len(nums), target, 0):
        print('Triplet exists')
    else:
        print('Triplet doesn\'t exist')