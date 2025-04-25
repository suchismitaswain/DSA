def countPairs(arr1, arr2, m, n, x): 
    count = 0

    for i in range(m): 
        for j in range(n): 

            if arr1[i] + arr2[j] == x: 
                count = count + 1

    return count 

arr1 = [1, 3, 5, 7] 
arr2 = [2, 3, 5, 8] 
m = len(arr1) 
n = len(arr2) 
x = 10
print("Count = ",  
        countPairs(arr1, arr2, m, n, x)) 