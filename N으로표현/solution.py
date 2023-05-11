from collections import defaultdict
from math import ceil
def solution(N, number):
    d = defaultdict(set)
    d[1].add(N)
    if N==number: return 1
    for i in range(2, 9):
        d[i].add(int(f"{N}"*i))
        if number==int(f"{N}"*i): return i
        for j in range(i-1, ceil(i/2)-1, -1):
            k = i-j
            for n1 in d[j]:
                for n2 in d[k]:
                    if n1+n2==number: return i
                    d[i].add(n1+n2)
                    if n1*n2==number: return i
                    d[i].add(n1*n2)
                    if abs(n1-n2)==number: return i
                    if n1!=n2: d[i].add(abs(n1-n2))
                    if n2>=n1:
                        if n2//n1==number: return i
                        d[i].add(n2//n1)
                    else:
                        if n1//n2==number: return i
                        d[i].add(n1//n2)
    return -1
