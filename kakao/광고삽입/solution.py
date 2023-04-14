from collections import deque

def get_seconds(t):
    h, m, s = map(int, t.split(":"))
    return h*3600+m*60+s

def solution(play_time, adv_time, logs):
    total = get_seconds(play_time)
    adv = get_seconds(adv_time)
    times = [0]*(total+1)
    ans = 0
    answer = 0
    for log in logs:
        start, end = map(lambda x: get_seconds(x), log.split("-"))
        times[start]+=1
        times[end]-=1
    for i in range(1, total+1):
        times[i]+=times[i-1]
    s = sum(times[:adv-1])
    ans = s
    for i in range(1, total-adv+1):
        s =  s-times[i-1]+times[i+adv-1]  # 시간초과 예상구간
        if ans<s:
            ans=s
            answer=i
    h = answer//3600
    m = (answer%3600)//60
    s = (answer%3600)%60
    return "%02d:%02d:%02d"%(h,m,s)
