def solution(s):
    d = {"(": ")", "{": "}", "[": "]"}
    answer = 0
    l = len(s)
    s += s
    for i in range(l):
        stk = []
        s_ = s[i:l+i]
        for j in s_:
            if j in d.keys():
                stk.append(j)
            else:
                if (not stk) or (j != d[stk[-1]]):
                    break
                stk.pop()
        else:
            if not stk:
                answer += 1
                
    return answer