def solution(s):
    answer = []
    d = {}
    for idx, ch in enumerate(s):
        if d.get(ch):
            answer.append(idx + 1 - d[ch])
        else:
            answer.append(-1)
        d[ch] = idx + 1
    return answer
