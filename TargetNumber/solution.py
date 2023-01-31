def dfs(idx, arr, total, target):
    if idx == len(arr):
        if total == target:
            return 1
        else: 
            return 0
    cnt = 0
    cnt += dfs(idx+1, arr, total+arr[idx], target)
    cnt += dfs(idx+1, arr, total-arr[idx], target)
    return cnt

def solution(numbers, target):
    return dfs(0, numbers, 0, target)
