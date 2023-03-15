def solution(scores):
    wanho = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    m = 1; answer = 1
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        if m <= s[1]:
            if sum(wanho) < s[0] + s[1]:
                answer += 1
            m = s[1]
    return answer
