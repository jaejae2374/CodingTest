def solution(matrix_sizes):
    def dp(x, y):
        if (x, y) in cache:
            return cache[(x, y)]
        if x==y:
            return 0
        minimum=10**9
        for i in range(x, y):
            val = dp(x, i)+dp(i+1, y)+matrix[x][0]*matrix[i+1][0]*matrix[y][1]
            if val < minimum:
                minimum = val
                cache[(x, y)] = minimum
        return cache[(x, y)]
    
    matrix = matrix_sizes
    cache = {}
    answer = dp(0, len(matrix)-1)
    return answer
