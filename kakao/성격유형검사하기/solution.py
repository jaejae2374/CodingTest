from collections import defaultdict

def solution(survey, choices):
    indicators = ["RT", "CF", "JM", "AN"]
    answer = ""
    d = defaultdict(int)
    for s, c in zip(survey, choices):
        if c-4 > 0:
            d[s[1]] += c-4
        elif c-4 < 0:
            d[s[0]] += 4-c
    
    for i in indicators:
        if d[i[0]] >= d[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer
    