def dynamic_partial_sum(arr):
    cache = [0] * len(arr)
    cache[0] = arr[0]
    for i in range(1, len(arr)):
        cache[i] = max(0, cache[i-1]) + arr[i]
    return max(cache)

def solution(sequence):
    l = len(sequence)
    p = [1, -1] * (l//2)
    if l % 2 == 1:
        p.append(1)
    sequence1 = list(map(lambda x: x[0]*x[1], zip(sequence, p)))
    sequence2 = list(map(lambda x: x[0]*x[1]*(-1), zip(sequence, p)))
    return max(dynamic_partial_sum(sequence1), dynamic_partial_sum(sequence2))
