from collections import deque

def solution(s):
    answer = deque()
    for sen in s:
        cnt = 0
        stk = deque(["-1", "-1"])
        for ch in sen:
            stk.append(ch)
            if ch == "0":
                if stk[-3] == "1" and stk[-2] == "1":
                    for _ in range(3): stk.pop()
                    cnt += 1
        stk = list(stk)[2:]
        for i in range(len(stk)-1, -1, -1):
            if stk[i] == '0':
                break
        else:
            i = -1        
        answer.append("".join(stk[:i+1] + ["1", "1", "0"]*cnt + stk[i+1:]))
    return list(answer)
