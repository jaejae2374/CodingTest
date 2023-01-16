from itertools import zip_longest

def toList(l):
    new_l = []
    for idx, val in enumerate(l):
        new_l += [idx+1]*val
    return new_l
    
def solution(cap, n, deliveries, pickups):
    deliveries = toList(deliveries)
    pickups = toList(pickups)
    deliveries = deliveries[::-cap]
    pickups = pickups[::-cap]
    return sum(map(lambda x: max(x), zip_longest(deliveries, pickups, fillvalue=0)))*2

