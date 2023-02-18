from collections import deque

def solution(cacheSize, cities):
    cache = [0]*cacheSize
    cache = deque(cache)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.appendleft(city)
        else:
            answer += 5
            cache.appendleft(city)
            cache.pop()
    return answer
