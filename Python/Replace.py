import sys

def replace(nums):

    for i in range(len(nums)):
 
        successor = -1
        diff = sys.maxsize
 
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i] and (nums[j] - nums[i] < diff):
                successor = nums[j]
                diff = nums[j] - nums[i]
 
        nums[i] = successor
 
    print(nums)
 
 
if __name__ == '__main__':
 
    nums = [10, 100, 93, 32, 35, 65, 80, 90, 94, 6]
    replace(nums)