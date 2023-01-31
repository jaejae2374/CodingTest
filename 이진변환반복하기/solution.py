def solution(s):
    cnt = 0
    zeros = 0
    while s!="1":
        ones = s.count("1")
        zeros += (len(s)-ones)
        s = "{0:b}".format(s.count("1"))
        cnt += 1
    return [cnt, zeros]
