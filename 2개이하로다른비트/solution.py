def solution(numbers):
    answer = []
    for n in numbers:
        if n%2 == 0:
            answer.append(n+1)
        else:
            tmp = "0" + str(bin(n))[2:]
            idx = len(tmp) - tmp.rfind("01") - 2
            answer.append(n+(2**idx))
    return answer
