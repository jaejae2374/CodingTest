def solution(cap, n, deliveries, pickups):
    answer = 0
    while True:
        d = 0
        deliver = cap
        pickup = cap
        for idx in range(len(deliveries)-1, -1, -1):
            if 0 < deliveries[idx] <= deliver:
                deliver -= deliveries[idx]
                deliveries[idx] = 0
                d = max(idx+1, d)
            elif deliveries[idx] > deliver:
                deliveries[idx] -= deliver
                deliver = 0
                d = max(idx+1, d)
            if deliver == 0:
                deliveries = deliveries[:idx+1]
                break
            if idx == 0:
                deliveries = []
                break
                
        for idx in range(len(pickups)-1, -1, -1):
            if 0 < pickups[idx] <= pickup:
                pickup -= pickups[idx]
                pickups[idx] = 0
                d = max(idx+1, d)
            elif pickups[idx] > pickup:
                pickups[idx] -= pickup
                pickup = 0
                d = max(idx+1, d)
            if pickup == 0:
                pickups = pickups[:idx+1]
                break
            if idx == 0:
                pickups = []
                break
        if d == 0:
            break
        answer += d
    return answer*2
