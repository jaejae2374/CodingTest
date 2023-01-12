def solution(n, info):
    answer = [0]*len(info)
    
    # 한 발당 단가 구하기
    info_per = []
    info_ryan = list(map(lambda x: x+1, info))
    for idx, cnt in enumerate(info_ryan):
        if cnt > 1:
            info_per.append((10-idx)*2/cnt)
        else:
            info_per.append((10-idx)/cnt)
        
    while True:
        # 단가 max인 값 구하기
        m = max(info_per)
        if m == 0:
            break
        
        # find를 뒤에서부터 하기 rfind
        num = info_per.count(m)
        for j in range(num):
            i = info_per.index(m)
        
        # 이미 쏜건지 체크
        # 발수 남았는지 체크
        if info_ryan[i] <= n:
            n -= info_ryan[i]
            answer[i] = info_ryan[i]
        info_per[i] = 0
            
        if n == 0:
            break
    if n > 0:
        answer[-1] += n
    ryan_total = 0
    for idx, cnt in enumerate(answer):
        if cnt:
            ryan_total+=(10-idx)
    peach_total = 0
    for idx, cnt in enumerate(zip(info ,answer)):
        if cnt[0]:
            if cnt[0] - cnt[1] >= 0:
                peach_total += 10-idx
    if peach_total >= ryan_total:
        return [-1]
    return answer
