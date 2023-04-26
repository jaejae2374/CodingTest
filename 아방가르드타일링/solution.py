from collections import defaultdict

def solution(n):
    d = defaultdict(int)
    d[1] = 1; d[2] = 3; d[3] = 10; d[0] = 1;
    d[4] = 23; d[5] = 62; d[6] = 170
    if n<7:
        return d[n]
    for i in range(7, n+1):
        d[i] = (d[i-1]+2*d[i-2]+5*d[i-3])%1000000007
        d[i] += (d[i-3] + d[i-4] - d[i-6]) % 1000000007
        d[i] %= 1000000007
    return d[n]
    