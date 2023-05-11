from math import inf

def get_digit(number):
    cnt = 0
    while (number>0):
        number//=10
        cnt+=1
    
    return cnt

def search(N, number, cnt):
    if cnt>8:
        return inf
    if number==0:
        return cnt
    l = get_digit(number)
    if number==int(f"{N}"*l):
        return l+cnt
    print(number, cnt)
    results = []
    results.append(search(N, number*N, cnt+1))
    if number%N==0:
        results.append(search(N, number//N, cnt+1))
    results.append(search(N, number+N, cnt+1))
    if number-N>0:
        results.append(search(N, number-N, cnt+1))
    
    return min(results)
    

def solution(N, number):
    # if 5==int(f"{5}"*1): return -1
    answer = search(N, number, 0)
    if answer>8: return -1
    return answer

print(solution(5, 12))