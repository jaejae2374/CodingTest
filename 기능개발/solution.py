def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 1
        p = progresses.pop(0)
        s = speeds.pop(0)
        r = 100 - p
        if r % s == 0:
            days = int(r / s)
        else:
            days = int(r//s) + 1
        while progresses:
            if progresses[0] + speeds[0]*days >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        answer.append(cnt)
    return answer
