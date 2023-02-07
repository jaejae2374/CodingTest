from math import sqrt
from itertools import permutations

def isPrime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)
    results = set()
    
    for i in range(1, len(numbers)+1):
        cases = permutations(nums, i)
        for case in cases:
            n = int("".join(case))
            if isPrime(n):
                results.add(n)
    return len(results)
