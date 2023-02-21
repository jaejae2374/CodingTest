def solution(weights):
    d = {}; same = {}; answer = 0
    
    for w in weights:
        same[w] = same[w] + 1 if same.get(w) else 1
        d[w*2] = d[w*2] + 1 if d.get(w*2) else 1
        d[w*3] = d[w*3] + 1 if d.get(w*3) else 1
        d[w*4] = d[w*4] + 1 if d.get(w*4) else 1
        
    for k in d:
        if d[k] >= 2:
            answer += int((d[k] * (d[k]-1)) / 2)
            
    for k in same:
        if same[k] >= 2:
            answer -= (same[k] * (same[k]-1))
            
    return answer
