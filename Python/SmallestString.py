from collections import defaultdict
from typing import List

def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        visited = [False]*n
        canGo = defaultdict(list)
        mainList = []
        
        for i,j in pairs:
            canGo[i].append(j)
            canGo[j].append(i)
        
        def dfs(node,path):
            visited[node] = True
            path.append(node)
            for adj in canGo[node]:
                if visited[adj] == False:
                    dfs(adj,path)
        
        for i in range(n):
            if visited[i] == True: continue
            path = []
            dfs(i,path)
            mainList.append(path)

        for lst in mainList:
            lst.sort()
            tmp = [s[i] for i in lst]
            tmp.sort()
            for i in range(len(lst)):
                s = s[:lst[i]]  + tmp[i] + s[lst[i]+1:]
        return s
        