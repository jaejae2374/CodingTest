import heapq
def solution(jobs):
    answer = 0
    queue = []
    t = 0; idx=0
    jobs.sort(key=lambda x: (x[0], x[1]))
    n = len(jobs)
    while idx<n:
        request, time = jobs[idx]
        if not queue and t<=request:
            t = request+time
            answer += time
            idx+=1
            continue
        if t>=request:
            heapq.heappush(queue, [time, request])
            idx+=1
        else:
            time, request = heapq.heappop(queue)
            answer += t-request+time
            t += time
    while queue:
        time, request = heapq.heappop(queue)
        answer += t-request+time
        t += time
    return answer//n
