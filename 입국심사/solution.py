def solution(n, times):
    answer = 0
    min_t=times[0]
    max_t=times[0]*n
    while True:
        cnt = 0
        mid = (min_t+max_t) // 2
        for i in times:
            cnt += (mid//i)
        if cnt >= n:
            max_t=mid
        else:
            min_t=mid
        if min_t == max_t-1:
            return max_t
