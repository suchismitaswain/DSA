from collections import defaultdict
from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        students = defaultdict(lambda: [])
        kthScores = []
        
        for item in score:
            students[item[k]] = item
            kthScores.append(item[k])
        kthScores.sort()
        
        for i in range(len(kthScores)):
            score[len(score) - 1 - i] = students[kthScores[i]]
            
        return score
