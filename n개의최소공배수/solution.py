from functools import reduce

def gcd(a, b): 
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

def solution(arr):
    return reduce(lambda x, y: lcm(x,y), arr)
