def solution(n):
    if n % 2 == 1:
        return 0
    d = {2: 3, 4: 11}
    if n >= 6:
        for i in range(6, n+1):
            if i % 2 == 1:
                continue
            else:
                d[i] = (d[i-2]*4 - d[i-4]) % 1000000007
    return d[n]
