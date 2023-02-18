from itertools import permutations
from collections import deque

def solution(expression):
    answer = []
    priorities = permutations(["*", "+", "-"], 3)
    for p in priorities:
        priority = {p[0]: 3, p[1]: 2, p[2]: 1}
        operand = ""; operands = deque(); operators = deque()
        for e in expression:
            if e.isnumeric():
                operand += e
            else:
                operands.append(operand)
                operand = ""
                while operators:
                    if priority[operators[-1]] >= priority[e]:
                        opt = operators.pop()
                        op2 = operands.pop()
                        op1 = operands.pop()
                        operands.append(str(eval(op1+opt+op2)))
                    else: break
                operators.append(e)
        operands.append(operand)

        while operators:
            opt = operators.pop()
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(str(eval(op1+opt+op2)))
        answer.append(abs(int(operands[0])))
    return max(answer)
