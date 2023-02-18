def solution(n):
    idx = 1
    while True:
        n -= (3**idx)
        if n <= 0:
            n += (3**idx)
            break
        idx += 1
    answer = ""
    for i in range(1, idx+1):
        if n <= 3**(idx-i):
            answer += "1"
        elif n <= (3**(idx-i))*2:
            answer += "2"
            n -= 3**(idx-i)
        else:
            answer += "4"
            n -= (3**(idx-i))*2
            
    return answer
