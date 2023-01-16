def algorithm1(sen):
    """step 1 to 4"""
    l, r = 0, 0
    if len(sen) == 0:
        return sen
    for idx, s in enumerate(sen):
        if s == "(":
            l+=1
        else:
            r+=1
        if l==r:
            break
    if check(sen[:idx+1]):
        return sen[:idx+1] + algorithm1(sen[idx+1:])
    else:
        result = f"({algorithm1(sen[idx+1:])})"
        for s in sen[:idx+1][1:-1]:
            if s == "(":
                result += ")"
            else:
                result += "("
        return result

def check(sen):
    """Check whether it is correct"""
    stk = []
    for s in sen:
        if s == "(":
            stk.append(s)
        else:
            if not stk:
                return False
            stk.pop()
    if stk:
        return False
    return True

def solution(p):
    return algorithm1(p)
