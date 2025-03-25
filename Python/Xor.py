from math import log
 
 
def log2(x, base):
    return int(log(x) // log(base))

def findDuplicates(arr, n):

    result = arr[0] ^ arr[n + 1]
    for i in range(1, n + 1):
        result = result ^ arr[i] ^ i

    x = y = 0
 
    k = log2(result & -result, 2)
 
    for i in range(n + 2):

        if arr[i] & (1 << k):
            x = x ^ arr[i]
 
        else:
            y = y ^ arr[i]

    for i in range(1, n + 1):
 
        if i & (1 << k):
            x = x ^ i
 
        else:
            y = y ^ i
 
    print(f'The duplicate elements are {x} and {y}')
 
 
if __name__ == '__main__':
 
    arr = [4, 3, 6, 5, 2, 4, 1, 1]
    n = 6        # list size is `n+2`
 
    findDuplicates(arr, n)