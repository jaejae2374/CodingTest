def solution(record):
    d = {}
    for r in record:
        if r.startswith("Enter") or r.startswith("Change"):
            _, uid, name = r.split(" ")
            d[uid] = name
    
    answer = []
    for r in record:
        if r.startswith("Enter"):
            _, uid, _ = r.split(" ")
            answer.append(f"{d[uid]}님이 들어왔습니다.")
        elif r.startswith("Leave"):
            _, uid = r.split(" ")
            answer.append(f"{d[uid]}님이 나갔습니다.")
    
    return answer
