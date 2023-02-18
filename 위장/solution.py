def solution(clothes):
    d = {}
    for cloth in clothes:
        if d.get(cloth[1]):
            d[cloth[1]].append(cloth[0])
        else:
            d[cloth[1]] = [cloth[0]]
    answer = 1
    for k in d:
        answer *= (len(d[k]) + 1)
    return answer - 1
