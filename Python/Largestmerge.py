class Solution(object):
    def largestMerge(self, word1, word2):
        
        i=j=0
        s=""
		
        while i<len(word1) and j<len(word2):
		
            if word1[i] > word2[j]:
                s+=word1[i]
                i=i+1
				
            elif word1[i] < word2[j]:
                s+=word2[j]
                j=j+1
				
            elif word1[i:] > word2[j:]:
                s+=word1[i]
                i+=1
				
            else:
                s+=word2[j]
                j+=1
        
        while i<len(word1):
            s=s+word1[i]
            i=i+1
			
        while j<len(word2):
            s=s+word2[j]
            j=j+1
			
        return s
        