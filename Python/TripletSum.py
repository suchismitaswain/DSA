def closest3Sum(arr, target):
    n = len(arr)
    minDiff = float('inf')
    res = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                currSum = arr[i] + arr[j] + arr[k]
                currDiff = abs(currSum - target)

                if currDiff < minDiff:
                    res = currSum
                    minDiff = currDiff
               
                elif currDiff == minDiff:
                	res = max(res, currSum)

    return res

if __name__ == "__main__":
	arr = [-1, 2, 2, 4]
	target = 4
	print(closest3Sum(arr, target))