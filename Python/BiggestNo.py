from functools import cmp_to_key

def my_compare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1  
    else:
        return 1

def findLargest(arr):
    numbers = [str(ele) for ele in arr]

    numbers.sort(key=cmp_to_key(my_compare))

    if numbers[0] == "0":
        return "0"

    res = "".join(numbers)

    return res

if __name__ == "__main__":
    arr = [3, 30, 34, 5, 9]
    print(findLargest(arr))