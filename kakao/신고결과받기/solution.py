from collections import defaultdict

def solution(id_list, report, k):
    mails = defaultdict(int)
    reports = defaultdict(set)
    
    for r in report:
        sj, oj = r.split(" ")
        reports[oj].add(sj)
        
    for oj in reports:
        if len(reports[oj]) >= k:
            for sj in reports[oj]:
                mails[sj] += 1
    answer = [mails[id] for id in id_list]            
    return answer
