from itertools import combinations

def solution(relation):
    idx = 1
    row = len(relation)
    cols = [i for i in range(len(relation[0]))]
    answer = 0
    used = []
    while idx <= len(cols):
        for col in combinations(cols, idx):
            isExist = False
            for us in used:
                for u in us:
                    if u not in col:
                        break
                else:
                    isExist = True
                    break
            if isExist: continue
            results = set(map(lambda x: tuple([x[c] for c in col]), relation))
            if len(results) == row:
                answer += 1
                if len(col)==1:
                    cols.remove(col[0])
                else:
                    used.append(col)
        idx += 1
    return answer