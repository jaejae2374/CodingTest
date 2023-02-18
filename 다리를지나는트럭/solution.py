from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    q.append(truck_weights[0])
    fin = len(truck_weights) - 1
    idx = 0; total = truck_weights[0]; answer = 1;
    while total != 0:
        answer += 1
        if len(q) == bridge_length:
            total -= q.popleft()
        if idx != fin and total + truck_weights[idx+1] <= weight:
            total += truck_weights[idx+1]
            q.append(truck_weights[idx+1])
            idx += 1
        else:
            q.append(0)
    return answer
