def solution(card, n):
    # 여기에 코드를 작성해주세요.
    from collections import Counter
    ns = str(n)
    card.sort()
    card = "".join(map(lambda x: str(x), card))
    cn = Counter(ns)
    cc = Counter(card)
    for s in ns:
        if cc[s] != cn[s]:
            return -1
    from itertools import permutations
    cases = permutations(card, len(card))
    answer = 1
    for case in cases:
        if n==int("".join(case)):
            return answer
        answer+=1
    return answer