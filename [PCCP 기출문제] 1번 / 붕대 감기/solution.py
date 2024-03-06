def solution(bandage, health, attacks):
    t, x, y = bandage    
    before_atk = 0; answer = health
    for atk_time, demage in attacks:
        htime=atk_time-before_atk-1
        answer+=(htime)*x
        if htime>=t:
            answer+=(htime//t)*y
        answer=min(answer, health)
        answer-=demage
        before_atk=atk_time
        if answer<=0: return -1
    return answer
