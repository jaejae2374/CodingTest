from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    start = 1
    while (start <= n):
        start *= k
    start /= k
    
    tmp = 0
    while n>0:
        val, n = divmod(n, start)
        if 0 < val:
            tmp = tmp*10 + val
        elif val == 0:
            if tmp != 0:
                if is_prime(tmp):
                    answer += 1
                tmp = 0
        start /= k
    if is_prime(tmp):
        answer += 1
    return answer
