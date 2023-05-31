import heapq
def solution(n, works):
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)
    for _ in range(n):
        w = heapq.heappop(works)
        w = abs(w)-1
        if w!=0:
            heapq.heappush(works, -w)
        if not works:
            break
    answer = 0
    for w in works:
        answer += w**2
    return answer
