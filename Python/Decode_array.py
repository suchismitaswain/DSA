from math import sqrt

def decode(inp):

    m = len(inp)
    if m in (0, 2):
        return

    n = int((sqrt(8 * m + 1) + 1) / 2)
    A = [0] * n

    if n == 1 or m == 1:
        A[0] = inp[0]
    elif n == 2:
        A[0] = inp[0] - inp[1]
    else:
        A[0] = (inp[0] + inp[1] - inp[n - 1]) // 2

    for i in range(1, n):
        A[i] = inp[i - 1] - A[0]

    print(A)
 
 
if __name__ == '__main__':
 
    inp = [3, 4, 5, 6, 5, 6, 7, 7, 8, 9]
    decode(inp)