def get_cnt(n, i):
    result = 0
    idx = 5**(n-1)
    section = 1
    
    while True:
        if idx == i:
            for s in range(1, section+1):
                if s == 3: continue
                result += 4**(n-1)
            break
        elif idx*section > i:
            if section == 3:
                result += (4**(n-1))*2
                break
            else:
                for s in range(1, section):
                    if s == 3: continue
                    result += 4**(n-1)
                i -= idx*(section-1)
                section = 1
                n -= 1
                idx = 5**(n-1)
        else:
            section += 1
            
    return result

def solution(n, l, r):
    return get_cnt(n, r) - get_cnt(n, l-1)
