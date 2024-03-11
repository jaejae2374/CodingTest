def solution(n, tops):
    answer = 0
    # f(n+1) = 2*f(n) + g(n)
    # g(n+1) = f(n) + g(n)
    f = {}; g = {}
    f[0] = 1; g[0] = 1
    for i in range(1, n+1):
        if tops[i-1]:
            g[i] = f[i-1]*2+g[i-1]
            f[i] = g[i]+f[i-1]
        else: 
            g[i] = f[i-1]+g[i-1]
            f[i] = f[i-1]*2+g[i-1]
        g[i]%=10007
        f[i]%=10007
    return f[n]%10007