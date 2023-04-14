import sys
sys.setrecursionlimit(10**9)

weight = [
    [1,7,6,7,5,4,5,3,2,3],
    [7,1,2,4,2,3,5,4,5,6],
    [6,2,1,2,3,2,3,5,4,5],
    [7,4,2,1,5,3,2,6,5,4],
    [5,2,3,5,1,2,4,2,3,5],
    [4,3,2,3,2,1,2,3,2,3],
    [5,5,3,2,4,2,1,5,3,2],
    [3,4,5,6,2,3,5,1,2,4],
    [2,5,4,5,3,2,3,2,1,2],
    [3,6,5,4,5,3,2,4,2,1]
]
dp = {}
def dfs(numbers, i, left, right):
    if i == len(numbers):
        return 0
    if (i, left, right) in dp.keys():
        return dp[(i, left, right)]
    next_number = numbers[i]
    answer = 10**9
    if right != next_number:
        move_left =  weight[left][next_number]
        answer = min(answer, move_left + dfs(numbers, i+1, next_number, right))
    if left != next_number:
        move_right = weight[right][next_number]
        answer = min(answer, move_right + dfs(numbers, i+1, left, next_number))
    dp[(i, left, right)]= answer
    return answer

def solution(numbers):
    answer = 0
    numbers = [*map(int, numbers)]
    return dfs(numbers, 0, 4, 6)