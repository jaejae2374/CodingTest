# n = 1000,m = 1000 x=1,y=1 query = [[0,100001],[2,100001]]
def solution(n, m, x, y, queries):
    left, right = y, y
    up, down = x, x
    for d, q in queries[::-1]:
        if d==0:
            if left!=0:
                left+=q
            right = min(m-1, right+q)
        elif d==1:
            if right!=m-1:
                right-=q
            left = max(0, left-q)
        elif d==2:
            if up!=0:
                up+=q
            down = min(n-1, down+q)
        else:
            if down!=n-1:
                down-=q
            up = max(0, up-q)
        if up>down or left>right: return 0
    return (down-up+1)*(right-left+1)
    