def solution(n):
    next_ = n
    while True:
        next_+=1
        if bin(n).count('1') == bin(next_).count('1'):
            break
    return next_
