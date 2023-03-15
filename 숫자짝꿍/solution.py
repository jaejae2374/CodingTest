from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    l = []
    for k in x:
        if y.get(k):
            l += [k for _ in range(min(x[k], y[k]))]
    l.sort(reverse=True)
    if l:
        answer = "".join(l)
        if answer.startswith("0"):
            return "0"
        else: 
            return answer
    else:
        return "-1"
