import copy

def move_3_to_2(moves):
    return list(map(lambda x: x[::-1], moves))[::-1]

def move_2_to_3(moves):
    moves_ = copy.deepcopy(moves)
    for m in moves_:
        if m[0]==2:
            m[0]=1
        elif m[0]==1:
            m[0]=2
        else:
            pass
        if m[1]==2:
            m[1]=1
        elif m[1]==1:
            m[1]=2
        else:
            pass
    return moves_

def solution(n):
    d1_3 = {1: [[1, 3]], 2: [[1, 2], [1, 3], [2, 3]]}
    for i in range(3, n+1):
        d1_3[i] = d1_3[i-2] + [[1, 2]] + move_3_to_2(move_2_to_3(d1_3[i-2])) + [[1, 3]] + move_2_to_3(d1_3[i-1])
        
    return d1_3[n]
