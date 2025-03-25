import sys
from heapq import heappop, heappush
 
class Node:
    def __init__(self, value, list_num, index):
    
        self.value = value
        self.list_num = list_num
        self.index = index
 
    def __lt__(self, other):
        return self.value < other.value

def findMinimumRange(lists):
 
    if not lists:
        return -1, -1
 
    high = -sys.maxsize
 
    p = (0, sys.maxsize)
 
    pq = []
 
    for i in range(len(lists)):
        if not lists[i]:        
            return -1, -1
        heappush(pq, Node(lists[i][0], i, 0))
        high = max(high, lists[i][0])
 
    while True:
 
        top = heappop(pq)
 
        low = top.value
        i = top.list_num
        j = top.index
 
        if high - low < p[1] - p[0]:
            p = (low, high)
 
        if j == len(lists[i]) - 1:
            return p
 
        heappush(pq, Node(lists[i][j + 1], i, j + 1))
 
        high = max(high, lists[i][j + 1])
 
 
if __name__ == '__main__':
 
    lists = [[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]]
    print('The minimum range is', findMinimumRange(lists))