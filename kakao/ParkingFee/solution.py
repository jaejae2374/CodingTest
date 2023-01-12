import math
def solution(fees, records):
    answer = []
    cars = {}
    results = {}
    for record in records:
        r = record.split(' ')
        if r[2] == "IN":
            h, m = r[0].split(":")
            cars[r[1]] = int(h)*60 + int(m)
        else:
            h, m = r[0].split(":")
            total_m = int(h)*60 + int(m) - cars[r[1]]
            if results.get(r[1], False):
                results[r[1]] += total_m
            else:
                results[r[1]] = total_m
            del(cars[r[1]])
    for c in cars:
        if results.get(c, False):
                results[c] += 1439 - cars[c]
        else:
            results[c] = 1439 - cars[c]
        
    for r in results:
        total_f = 0
        if results[r] > fees[0]:
            total_f = fees[1] + math.ceil((results[r] - fees[0]) / fees[2]) * fees[3]
        else:
            total_f = fees[1]
        answer.append((r, total_f))
    return list(map(lambda x: x[1], sorted(answer, key=lambda x: x[0])))
