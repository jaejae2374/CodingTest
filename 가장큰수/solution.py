def solution(numbers):
    answer = []
    for n in numbers:
        if n // 10 == 0:
            tmp = f"{n}"*12
        elif n // 100 == 0:
            tmp = f"{n}"*6
        elif n // 1000 == 0:
            tmp = f"{n}"*4
        else:
            tmp = f"{n}"*3
        answer.append((tmp, str(n)))
    answer.sort(key=lambda x: x[0], reverse=True)
    return str(int(''.join(list(map(lambda x: x[1], answer)))))
