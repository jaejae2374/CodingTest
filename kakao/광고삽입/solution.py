from collections import deque

def get_seconds(t):
    h, m, s = map(int, t.split(":"))
    return h*3600+m*60+s

def solution(play_time, adv_time, logs):
    total = get_seconds(play_time)
    adv = get_seconds(adv_time)
    times = [0]*(total+1)
    for log in logs:
        start, end = map(lambda x: get_seconds(x), log.split("-"))
        times[start]+=1
        times[end]-=1
        
    std=0; ans=0; answer=0
    for i in range(1, total+1):
        times[i]+=times[i-1]
        if i<=adv:
            ans+=times[i-1]
            ans = std
        else:
            std =  std+times[i-1]-times[i-adv-1]
            if ans<std:
                answer = i-adv
                ans = std
    h = answer//3600
    m = (answer%3600)//60
    s = (answer%3600)%60
    return "%02d:%02d:%02d"%(h,m,s)


