def convert_one(sentence):
    result = ""
    zero_cnt = 0
    for s in sentence:
        if s=="1":
            result += s
        else:
            zero_cnt += 1
    return result, zero_cnt

def solution(s):
    zero_cnt = 0
    cnt = 0
    while s!="1":
        s, zero_cnt_ = convert_one(s)
        s = str(bin(len(s)))[2:]
        zero_cnt += zero_cnt_
        cnt += 1
    return [cnt, zero_cnt]
