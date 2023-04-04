from collections import Counter
def solution(participant, completion):
    c = Counter(participant) - Counter(completion)
    return c.most_common(1)[0][0]
