from collections import deque

def solution(sequence, k):
    answer = []
    q = deque()
    idx = deque()
    total = 0
    for i, n in enumerate(sequence):
        while (q and total+n>k):
            total -= q.popleft()
            idx.popleft()
        if total+n==k:
            if idx:
                answer.append([idx[0], i])
            else:
                answer.append([i, i])
        q.append(n)
        idx.append(i)
        total += n
        
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]
