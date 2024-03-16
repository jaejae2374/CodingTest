from itertools import combinations, product
from collections import Counter
def solution(dice):
    n = len(dice)
    dices = set(range(1, n+1))
    cases = list(combinations(range(1, n+1), n//2))
    cases = cases[:len(cases)//2]
    max_wins = 0; answer = None
    for diceA in cases:
        diceB = list(dices-set(diceA))
        diceA_list = [dice[d-1] for d in diceA]
        diceB_list = [dice[d-1] for d in diceB]
        diceA_sum = [sum(d) for d in product(*diceA_list)]
        diceB_sum = [sum(d) for d in product(*diceB_list)]
        dictA = Counter(diceA_sum); dictB = Counter(diceB_sum)
        winsA = 0; winsB = 0
        for ka, va in dictA.items():
            for kb, vb in dictB.items():
                if ka>kb:
                    winsA+=va*vb
                elif ka<kb:
                    winsB+=va*vb
        if winsA>winsB and winsA>max_wins:
            max_wins = winsA; answer = list(diceA)
        elif winsB>winsA and winsB>max_wins:
            max_wins = winsB; answer = diceB
    answer.sort()
    return answer
        