import sys

def getMaxDiff(A):
 
    diff = -sys.maxsize
 
    n = len(A)
    if n == 0:
        return diff
 
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[j] > A[i]:
                diff = max(diff, A[j] - A[i])
 
    return diff
 
 
if __name__ == '__main__':
 
    A = [2, 7, 9, 5, 1, 3, 5]
 
    diff = getMaxDiff(A)
    if diff != -sys.maxsize:
        print("The maximum difference is", diff)
 