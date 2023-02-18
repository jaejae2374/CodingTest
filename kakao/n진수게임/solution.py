def get_nbase(num, n):
    s = "0"
    alpha = "ABCDEF"
    for i in range(1, num+1):
        tmp = ""
        while True:
            d, m = divmod(i, n)
            if m >= 10:
                m = alpha[m-10]
            tmp = f"{m}" + tmp
            if d == 0: break
            i = d
        s += tmp
    return s

def solution(n, t, m, p):
    
    idx = 1; std = 1; total = t*m; tmp = 0
    while True:
        std *= n
        tmp += std
        if tmp >= total:
            break
    
    s = get_nbase(std, n)
    answer = ''; cnt = 0;
    for i in range(p-1, len(s), m):
        cnt += 1
        answer += s[i]
        if cnt == t:
            break
        
    return answer
