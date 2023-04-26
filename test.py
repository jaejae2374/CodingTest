from math import sqrt
def solution(r1, r2):
    answer = 0
    r1, r2 = max(r1, r2), min(r1, r2)
    start = -1*r1
    d1 = r1**2; d2 = r2**2
    print(int(sqrt(d2-(2**2))))
    for i in range(start, 0):
        for j in range(int(sqrt(d2-(2**2)))+1, (-1*start)+1):
            d = i**2+j**2
            if d>d1:
                break
            else:
                answer+=1
            
    return answer*4 + ((r1-r2)+1)*4

solution(2, 3)