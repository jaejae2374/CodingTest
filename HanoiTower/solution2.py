def hanoi(start, end, via, n):
    if n == 0:
        return []
    return hanoi(start, via, end, n-1) + [[start, end]] + hanoi(via, end, start, n-1)

def solution(n):
    return hanoi(1, 3, 2, n)

