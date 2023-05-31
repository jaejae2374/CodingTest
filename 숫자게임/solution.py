def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    idx = 0
    for a in A:
        if a<B[idx]:
            answer+=1
            idx+=1
    return answer
