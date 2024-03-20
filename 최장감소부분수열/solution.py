def solution(sequence):
    n = len(sequence)
    dp = [1] * n 

    for i in range(n):
        for j in range(i):
            if sequence[i] < sequence[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp) 
