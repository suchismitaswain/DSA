class Solution(object):
    def minDeletionSize(self, strs):
        a=len(strs[0])
        k=0
        l=[]
        for x in range(a):
            for y in strs:
                l.append(y[x])
            e=l[:]
            e.sort()
            if e!=l:
                k=k+1
            l=[]
        return k