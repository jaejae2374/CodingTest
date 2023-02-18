from bisect import bisect_left
def solution(info, query):
    results = []
    d = {}
    for lan in ["cpp", "java", "python", "-"]:
        for job in ["backend", "frontend", "-"]:
            for exp in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    d[lan+job+exp+food] = []
    for i in info:
        l = i.split(" ")
        for lan in [l[0], "-"]:
            for job in [l[1], "-"]:
                for exp in [l[2], "-"]:
                    for food in [l[3], "-"]:
                        d[lan+job+exp+food].append(int(l[4]))

    for key in d.keys():
        d[key].sort()
    for q in query:
        l = q.split(" and ")
        fs = l.pop()
        food, score = fs.split(" ")
        l.append(food)
        score = int(score)
        results.append(len(d[l[0]+l[1]+l[2]+l[3]]) - bisect_left(d[l[0]+l[1]+l[2]+l[3]], score))
        
    return results
