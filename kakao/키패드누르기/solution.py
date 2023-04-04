LEFT = [1, 4, 7]
RIGHT = [3, 6, 9]

def get_pos(n):
    r, c = divmod(n, 3)
    if n%3 == 0: 
        r -= 1
        c += 1
    return r, c

def solution(numbers, hand):
    answer = ''
    last_l = 10
    last_r = 12
    for n in numbers:
        if n in LEFT:
            last_l = n
            answer += "L"
        elif n in RIGHT:
            last_r = n
            answer += "R"
        else:
            if n == 0: n = 11
            r, c = get_pos(n)
            rl, cl = get_pos(last_l)
            rr, cr = get_pos(last_r)
            dl = abs(r-rl) + abs(c-cl)
            dr = abs(r-rr) + abs(c-cr)
            if dl > dr:
                answer += "R"
                last_r = n
            elif dl < dr:
                answer += "L"
                last_l = n
            else:
                if hand == "right":
                    answer += "R"
                    last_r = n
                else:
                    answer += "L"
                    last_l = n
    
    return answer
