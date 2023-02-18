def solution(s):
    answer = []
    for i in range(1, len(s)):
        new_s = ""
        before = ""; cnt = 1
        for idx in range(0, len(s), i):
            if idx + i > len(s):
                if cnt > 1:
                    new_s += f"{cnt}{before}"
                else:
                    new_s += before
                new_s += s[idx:]
                break
            if before == s[idx:idx+i]:
                cnt += 1
            else:
                if cnt > 1:
                    new_s += f"{cnt}{before}"
                else:
                    new_s += before
                cnt = 1
            before = s[idx:idx+i]
        else:
            if cnt > 1:
                new_s += f"{cnt}{before}"
            else:
                new_s += before
        answer.append(len(new_s))
        
    if not answer:
        return 1
    
    return min(answer)
