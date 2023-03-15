def solution(keymap, targets):
    answer = []
    d = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if d.get(key):
                if d[key] > i+1:
                    d[key] = i+1
            else:
                d[key] = i+1
    for target in targets:
        cnt = 0
        for ch in target:
            if d.get(ch):
                cnt += d[ch]
            else:
                answer.append(-1)
                break
        else:
            answer.append(cnt)
    return answer
