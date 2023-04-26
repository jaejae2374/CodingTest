from collections import deque
from math import inf

def choice(n):
    # 우선순위
    # 싱글1 > 더트1 > 싱글2 > 싱글1 더트1
    if n<=20 or n==50:
        return [1, 1]
    elif n%3==0 and n/3<=20:
        return [1, 0]
    elif n%2==0 and n/2<=20:
        return [1, 0]
    elif 50<n<60 or 20<n<40:
        return [2, 2]
    else:
        return [2, 1]

def solution(target):
    if target<=60: return choice(target)
    cnt = target//60
    l = [[cnt, 0, target%60]]
    l = deque(l)
    for i in range(cnt-1, -1, -1):
        tmp = target - 60*i
        d, m = divmod(tmp, 50)
        if m+50<=60:
            m+=50
            d-=1
        l.append([i, d, m])
    std = [inf, inf]
    for s60, s50, t in l:
        res = [s60+s50, s50]
        tmp = choice(t)
        res[0] += tmp[0]
        res[1] += tmp[1]
        if std[0]>res[0]:
            std = res
        elif std[0]==res[0]:
            if res[1]>std[1]:
                std=res
    return std
