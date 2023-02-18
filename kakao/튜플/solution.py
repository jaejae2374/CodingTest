from collections import Counter

def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    c = Counter()
    
    for ch in s:
        l = ch.split(",")
        tmp = Counter(l)
        c += tmp
    
    for i in c.most_common():
        if i[0].isdigit():
            answer.append(int(i[0]))
        
    return answer
