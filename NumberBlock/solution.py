from math import sqrt

def get_div(n):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    
    tmp = []
    for i in range(2, int(sqrt(n)) + 1):
        if n%i == 0:
            d = int(n/i)
            if d <= 10000000:
                return d
            else:
                tmp.append(i)
    if tmp:
        return tmp[-1]
    return 1

def solution(begin, end):
    answer = [get_div(i) for i in range(begin, end+1)]
    return answer
