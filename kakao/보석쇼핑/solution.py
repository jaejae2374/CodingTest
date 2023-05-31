from collections import Counter
from math import inf

def solution(gems):
    stones = len(set(gems))
    right = stones-1
    left = 0
    counter = Counter(gems[left:right+1])
    current = len(counter.keys())
    if current == stones:
        return [1, right+1]
    
    std = inf
    fin = len(gems)
    answer = [0, 0]
    while (left<fin):
        if current!=stones:
            for i in range(right+1, fin):
                if counter[gems[i]]==0:
                    current+=1
                counter[gems[i]]+=1
                if current==stones:
                    right = i
                    break
        if current==stones:
            if std>(right-left):
                std = right-left
                answer[0]=left+1
                answer[1]=right+1
        else:
            break
        counter[gems[left]]-=1
        if counter[gems[left]]==0:
            current-=1
        left+=1
        
    return answer
    