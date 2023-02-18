import math 

def solution(str1, str2):
    d = {}
    for i in range(len(str1)-1):
        s = str1[i:i+2]
        s = s.lower()
        if s.isalpha():
            if d.get(s):
                d[s][0] += 1
            else:
                d[s] = [1, 0]
    for i in range(len(str2)-1):
        s = str2[i:i+2]
        s = s.lower()
        if s.isalpha():
            if d.get(s):
                d[s][1] += 1
            else:
                d[s] = [0, 1]
    
    i = 0; u = 0
    for keyword in d:
        i += min(d[keyword])
        u += max(d[keyword])
    
    if u == 0: 
        answer = 65536
    else: 
        answer = math.floor((i/u) * 65536)
        
    return answer
