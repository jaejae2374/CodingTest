import sys
sys.setrecursionlimit(2001)

def solution(n, tolls):
    def dp(x, y, tolls):
        if x==1 and y==1: return tolls[0][0]
        elif x==1:
            return dp(x, y-1, tolls)+tolls[x-1][y-1]
        elif y==1:
            return dp(x-1, y, tolls)+tolls[x-1][y-1]
        else:
            return min(dp(x-1, y, tolls)+tolls[x-1][y-1], dp(x, y-1, tolls)+tolls[x-1][y-1])
    return dp(n, n, tolls)

print(solution(3, [[1, 8, 7], [2, 7, 6], [3, 4, 5]]))