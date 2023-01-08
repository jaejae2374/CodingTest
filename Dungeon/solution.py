def solution(k, dungeons):
    # 던전 최소 필요 체크
    # 충족하면 소모하고 재귀적 호출
    if not dungeons:
        return 0
    answers = []
    for idx, d in enumerate(dungeons):
        answer = 0
        dungeons_ = dungeons.copy()
        if d[0] <= k:
            del dungeons_[idx]
            answer += solution(k-d[1], dungeons_) + 1
        answers.append(answer)
    return max(answers)
