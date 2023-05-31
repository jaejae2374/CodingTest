from math import ceil

def solution(n, s):
    if n>s: return [-1]
    answer = []
    while n>1:
        answer.append(ceil(s/n))
        s-=ceil(s/n)
        n-=1
    answer.append(s)
    return sorted(answer)
