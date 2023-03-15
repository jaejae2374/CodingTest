def check(s):
    l = len(s)
    if l == 1:
        return 1
    root = l // 2
    if s[root] == "0":
        if s[root//2] == "1" or s[root+root//2+1] == "1":
            return -1
    left = check(s[:root])
    right = check(s[root+1:])
    if left == -1 or right == -1:
        return -1
    return 1

def solution(numbers):
    answer = []
    for num in numbers:
        s = bin(num)[2:]
        size = 1
        while len(s) > pow(2, size) - 1:
            size += 1
        while len(s) < pow(2, size) - 1:
            s = '0' + s
        if check(s) == 1:
            answer.append(1)
        else:
            answer.append(0)
    return answer
