answer = [[0]*3 for i in range(3)]
for i in range(1, 3+1):
    for j in range(1, i+1):
        answer[j-1][i-1] = i
        answer[i-1][j-1] = i
        print(answer)
[[1, 2, 3], [2, 2, 3], [3, 3, 3]]