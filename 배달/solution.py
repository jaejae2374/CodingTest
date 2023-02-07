import heapq
def solution(N, road, K):
    graph = {i: {} for i in range(1, N+1)}
    for r in road:
        if not graph[r[0]].get(r[1]) or graph[r[0]][r[1]] > r[2]: 
            graph[r[0]][r[1]] = r[2]
        if not graph[r[1]].get(r[0]) or graph[r[1]][r[0]] > r[2]: 
            graph[r[1]][r[0]] = r[2]
    distances = [500001]*(N+1)
    distances[1] = 0
    queue = []
    heapq.heappush(queue, [distances[1], 1])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue
    
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return len(list(filter(lambda x: x<=K, distances)))
        

