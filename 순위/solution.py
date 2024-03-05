def solution(n, results):
    graph_1 = [[101 for _ in range(n)] for _ in range(n)]
    graph_2 = [[101 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph_1[i][i] = 0
        graph_2[i][i] = 0

    for w, l in results:
        graph_1[w-1][l-1] = 1
        graph_2[l-1][w-1] = 1
    for k in range(n):
        for s in range(n):
            for e in range(n):
                graph_1[s][e] = min(graph_1[s][e], graph_1[s][k]+graph_1[k][e])
                graph_2[s][e] = min(graph_2[s][e], graph_2[s][k]+graph_2[k][e])
    answer=0
    for i in range(n):
        for j in range(n):
            if graph_1[i][j]==101 and graph_2[i][j]==101:
                break
        else:
            answer+=1
                  
    return answer
