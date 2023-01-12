def solution(s):
    stk = []
    for i in s:
        if i == "(":
            stk.append(i)
        else:
            if not stk:
                return False
            stk.pop()
    if stk:
        return False
    return True
