import re

def solution(dartResult):
    weight = {"S": 1, "D": 2, "T": 3}
    answer = []
    pattern = re.compile("[0-9]+[A-Z][*#]?")
    while dartResult:
        s, e = pattern.match(dartResult).span()
        n = 0
        for c in dartResult[s:e]:
            if c.isdigit():
                n = n*10 + int(c)
            elif c.isalpha():
                n **= weight[c]
            else:
                if c == "*":
                    if answer:
                        answer[-1] *= 2
                    n *= 2
                else: 
                    n *= -1
        dartResult = dartResult[e:]
        answer.append(n)
    return sum(answer)
