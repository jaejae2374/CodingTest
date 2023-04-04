from collections import deque, Counter

def solution(picks, minerals):
    costs =[[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    l = len(minerals)
    orders = deque()
    for i in range(0, l, 5):
        m = minerals[i:] if i+5 > l else minerals[i:i+5]
        c = Counter(m)
        orders.append((c["diamond"], c["iron"], c["stone"]))
    for i in range(len(orders)-sum(picks)):
        orders.pop()
    orders = deque(sorted(orders, key=lambda x: (-x[0], -x[1], -x[2])))
    answer = 0
    for idx, pick in enumerate(picks):
        for i in range(pick):
            if not orders:
                return answer
            answer += sum(map(lambda x: costs[idx][x[0]]*x[1], enumerate(orders.popleft())))
    return answer
