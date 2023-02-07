from math import sqrt

def get_divisor(n):
    data = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            data.append(i)
    return data

def solution(brown, yellow):
    for v in get_divisor(yellow):
        h = int(yellow / v)
        if (h+2)*2 + v*2 == brown:
            return [h+2, v+2]
