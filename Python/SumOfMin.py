import sys

def sumOfMinAbsDifferences(arr, n):
    sum = 0
    for i in range(n):
        diff = sys.maxsize
        for j in range(n):
            if i != j:
                diff = min(diff, abs(arr[i] - arr[j]))
        sum += diff

    return sum

if __name__ == "__main__":
    arr = [5, 10, 1, 4, 8, 7]
    n = 6
 
    print("Sum =", sumOfMinAbsDifferences(arr, n))