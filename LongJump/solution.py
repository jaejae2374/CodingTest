def solution(n):
    # n칸 = (n-1)칸 + (n-2)
    d = {1: 1, 2: 2}
    if n > 2:
        for i in range(3, n+1):
            ans = d[i-2] + d[i-1]
            d[i] = ans % 1234567
    return d[n]
