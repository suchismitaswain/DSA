def maxProduct(arr):
    n = len(arr)
  
    result = arr[0]

    for i in range(n):
        mul = 1
      
        for j in range(i, n):
            mul *= arr[j]
        
            result = max(result, mul)
    
    return result

if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    print(maxProduct(arr))