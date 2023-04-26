from collections import deque
def solution(triangle):
    triangle_sum = deque(triangle[0])
    for row in triangle[1:]:
        l = len(row)
        triangle_sum.appendleft(0); triangle_sum.append(0)
        tmp = deque()
        for i in range(l):
            tmp.append(max(triangle_sum[i], triangle_sum[i+1])+row[i])
        triangle_sum = tmp
    return max(triangle_sum)
