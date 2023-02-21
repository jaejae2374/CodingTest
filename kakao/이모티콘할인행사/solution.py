def solution(users, emoticons):
    discounts = {"0": 10, "1": 20, "2": 30, "3": 40}
    u = len(users)
    n = len(emoticons)
    answer = []
    for i in range(4**n):
        std = 4; d = 1; s = "";
        while d:
            d, m = divmod(i, std)
            i = d
            s = str(m) + s
        s = "0"*(n-len(s)) + s
        sales = {}
        tmp = []; amount = 0; cnt = 0; emoticon_plus = []
        for discount, price in zip(s, emoticons):
            price_ = (price / 100) * (100-discounts[discount])
            for idx, user in enumerate(users):
                if idx in emoticon_plus: continue
                if user[0] <= discounts[discount]:
                    if sales.get(idx):
                        sales[idx] += price_
                    else:
                        sales[idx] = price_
                if sales.get(idx) and sales[idx] >= user[1]:
                    cnt += 1
                    emoticon_plus.append(idx)
                    sales[idx] = 0
        for idx in sales:
            amount += sales[idx]
        answer.append([cnt, int(amount)])
    
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[-1]
