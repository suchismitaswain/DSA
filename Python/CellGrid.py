class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
        NROW = len(grid)
        NCOL = len(grid[0])
        
        for row in grid:
            row.sort(reverse=True)
        
        @cache
        def calc(row,mask,presum):
            if row == NROW:
                return presum
                
            prd = calc(row+1,mask,presum)
            ret = prd
            for x in grid[row]:
                if (1<<x) & mask:
                    continue
                    
                if (x+prd) <= ret:
                    continue
                ret = max(ret, calc(row+1,mask | (1<<x), presum+x))
                
            return ret
    
        result = calc(0,0,0)
        return result