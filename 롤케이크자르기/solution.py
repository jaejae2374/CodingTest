from collections import Counter

def solution(topping):
    answer = 0
    d = Counter(topping)
    s = set()
    answer = 0

    for t in topping:
        d[t] -= 1
        s.add(t)
        if d[t] == 0:
            d.pop(t)
        if len(d) == len(s):
            answer += 1

    return answer
