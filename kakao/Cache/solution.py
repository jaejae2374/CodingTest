def solution(cacheSize, cities):
    cache = [0]*cacheSize
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache[:cacheSize]:
            answer += 1
        else:
            answer += 5
        cache.insert(0, city)
    return answer
