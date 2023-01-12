def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        a1 = arr1[i]
        for j in range(len(arr2[0])):
            a2 = list(map(lambda x: x[j], arr2))
            answer[i][j] = sum([x*y for x, y in zip(a1, a2)])
    return answer
