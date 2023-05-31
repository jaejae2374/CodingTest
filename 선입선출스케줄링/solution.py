def solution(n, cores):
    if n < len(cores):
        return n

    n -= len(cores)
    left, right = 1, min(cores) * n
    while left < right:
        mid = (right+left) // 2
        works = sum([mid // core for core in cores])

        if works < n:
            left = mid + 1
        else:
            right = mid

    work_hours = left
    n-=sum([(work_hours-1) // core for core in cores])

    for idx, core in enumerate(cores, start=1):
        if work_hours % core == 0:
            n -= 1
            if n == 0:
                return idx
            