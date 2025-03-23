def split_number(num, result):
 
    if num > 0:
        split_number(num // 10, result)
        result.append(num % 10)
 
def append(a, b, result):
 
    m = len(a)
    n = len(b)
 
    i = 0
    while i < m and i < n:
 
        total = a[i] + b[i]
 
        split_number(total, result)
        i = i + 1
 
    while i < m:
        split_number(a[i], result)
        i = i + 1
 
    while i < n:
        split_number(b[i], result)
        i = i + 1
 
 
if __name__ == '__main__':
 
    a = [23, 5, 2, 7, 87]
    b = [4, 67, 2, 8]

    result = []
    append(a, b, result)
    print(result)