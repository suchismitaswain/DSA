def findMax(arr, i):
 
    if i == len(arr) - 1:
        return arr[i]

    recMax = findMax(arr, i + 1)


    return max(recMax, arr[i])


def largest(arr):
    return findMax(arr, 0)

if __name__ == '__main__':
  arr = [10, 324, 45, 90, 9808]
  print(largest(arr))