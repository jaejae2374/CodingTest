def solution(arr):
    l = len(arr)
    zero_cnt = 0
    one_cnt = 0
    s = sum(map(lambda x: sum(x), arr))
    if s == l**2:
        return [0, 1]
    elif s == 0:
        return [1, 0]
    else:
        l = int(l / 2)
        box_1 = solution(list(map(lambda x: x[:l], arr))[:l])
        box_2 = solution(list(map(lambda x: x[l:], arr))[:l])
        box_3 = solution(list(map(lambda x: x[:l], arr))[l:])
        box_4 = solution(list(map(lambda x: x[l:], arr))[l:])
        zero_cnt += box_1[0] + box_2[0] + box_3[0] + box_4[0]
        one_cnt += box_1[1] + box_2[1] + box_3[1] + box_4[1]
        
    return [zero_cnt, one_cnt]
