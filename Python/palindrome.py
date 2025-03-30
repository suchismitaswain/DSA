def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def countPS(s):
    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i + 1, n):
        
            if isPalindrome(s, i, j):
                res += 1

    return res

if __name__ == "__main__":
    s = "abaab"
    print(countPS(s))