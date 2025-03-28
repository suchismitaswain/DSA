def median(mat):

    arr = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            arr.append(mat[i][j])
 
    arr.sort()

    mid = len(arr) // 2
    return arr[mid]
  
if __name__ == "__main__":
    mat = [[1, 3, 5],
           [2, 6, 9],
           [3, 6, 9]]
    print(median(mat))