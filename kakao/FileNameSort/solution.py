def solution(files):
    answer = []
    for file in files:
        n, t = 0, 0
        for idx, f in enumerate(file):
            if not n and f.isnumeric():
                n = idx
            if n and not f.isnumeric():
                t = idx
                break
        if t:
            file_ = [file[:n], file[n:t], file[t:]]
        else:
            file_ = [file[:n], file[n:], ""]
        answer.append(file_)
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return list(map(lambda x: "".join(x), answer))
