
def solution(info, query):
    answer = []
    info_ = list(map(lambda x: x.split(" "), info))
    for q in query:
        info_f = info_
        q = q.split(" ")
        idx = 0
        for p in q[:-1]:
            if p == "and": continue
            if p != "-":
                info_f = list(filter(lambda x: x[idx] == p, info_f))
            idx += 1
        answer.append(len(list(filter(lambda x: int(x[-1])>=int(q[-1]), info_f))))
    return answer

# 효율성 초과