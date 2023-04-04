def solution(n, lost, reserve):
    lost_ = list(set(lost) - set(reserve))
    reserve_ = list(set(reserve) - set(lost))
    lost_.sort(); reserve_.sort()
    lo = len(lost_)
    for l in lost_:
        if l-1 in reserve_:
            lo -= 1
            reserve_.remove(l-1)
        elif l+1 in reserve_:
            lo -= 1
            reserve_.remove(l+1)
    return n - lo
