def solution(n, wires):
    
    # for 문으로 하나 끊기
    # 끊은 edge 양 꼭지점을 헤드로 하는 트리 dfs
    
    answer = 101
    global visited
    for wire in wires:
        visited = {}
        for i in range(n):
            visited[i+1] = False
        first_tree = wire[0]
        second_tree = wire[1]
        wires_ = wires.copy()
        wires_.remove(wire)
        first_nodes = check_node(first_tree, wires_, visited) + 1
        second_nodes = check_node(second_tree, wires_, visited) + 1
        answer = min(answer, abs(first_nodes-second_nodes))
        
    return answer

def check_node(n, wires, visited):
    
    num = 0
    search_list = list(filter(lambda x: x[0]==n or x[1]==n, wires))
    visited[n] = True
    for s in search_list:
        if s[0] == n:
            next_n = s[1]
        else:
            next_n = s[0]
        if not visited[next_n]:
            num += check_node(next_n, wires, visited) + 1
    return num
    