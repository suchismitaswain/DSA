def merge(v, ans, l, mid, h):
    t = []  
    i = l
    j = mid+1
    while (i < mid+1 and j <= h):
    
        if v[i][0] > v[j][0]:
            ans[v[i][1]] += (h-j+1)
            t.append(v[i])
            i += 1
        else:
            t.append(v[j])
            j += 1

    while (i <= mid):
        t.append(v[i])
        i += 1

    while j <= h:
        t.append(v[j])
        j += 1

    k = 0
    i = l
    while (i <= h):
        v[i] = t[k]
        i += 1
        k += 1

def mergesort(v, ans, i, j):
    if i < j:
        mid = (i+j)//2

        mergesort(v, ans, i, mid)
        mergesort(v, ans, mid + 1, j)
        merge(v, ans, i, mid, j)


def constructLowerArray(arr, n):
    v = []

    for i in range(n):
        v.append([arr[i], i])

    ans = [0]*n

    mergesort(v, ans, 0, n-1)
    return ans


arr = [12, 1, 2, 3, 0, 11, 4]
n = len(arr)
ans = constructLowerArray(arr, n)
for x in ans:
    print(x, end=" ")