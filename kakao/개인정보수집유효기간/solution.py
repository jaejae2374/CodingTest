def solution(today, terms, privacies):
    answer = []
    t = {}
    for term in terms:
        name, duration = term.split(" ")
        t[name] = int(duration)
        
    t_year, t_month, t_day = map(int, today.split("."))
    for idx, privacy in enumerate(privacies, start=1):
        date, name = privacy.split(" ")
        year, month, day = map(int, date.split("."))
        y, m = divmod(month + t[name], 12)
        if m == 0:
            m = 12
            y -= 1
        if day-1 == 0:
            if m == 1:
                m = 12
                y -= 1
            else:
                m -= 1
            day = 28
        else:
            day -= 1
        year += y
        if t_year > year:
            answer.append(idx)
        elif t_year == year and t_month > m:
            answer.append(idx)
        elif t_year == year and m == t_month and t_day > day:
            answer.append(idx)
        
    return answer
