import string

def solution(msg):
    d = {}
    for i, a in enumerate(string.ascii_uppercase):
        d[a] = i+1
    i = 27; idx = 0; s = ""; l = len(msg);
    answer = []
    while idx < l:
        s += msg[idx]
        if d.get(s, False):
            idx += 1
        else:
            answer.append(d[s[:-1]])
            d[s] = i
            s = ""
            i += 1
    if s:
        answer.append(d[s])
    return answer
