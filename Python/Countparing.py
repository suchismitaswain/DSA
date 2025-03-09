def countPairs(arr, target):
    n = len(arr)
    cnt = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                cnt += 1
    return cnt

if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    target = 6
    print(countPairs(arr, target))