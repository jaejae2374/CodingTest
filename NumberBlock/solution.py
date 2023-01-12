from math import sqrt

def get_block(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return n / i
    return 1

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(get_block(i))
    return answer
