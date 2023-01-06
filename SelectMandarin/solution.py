from collections import Counter

def solution(k, tangerine):
    
    count = Counter(tangerine)
    answer = []
    for kg, n in count.most_common():
        k-=n
        answer.append(kg)
        if k <= 0:
            break
    return len(answer)
