from collections import deque, defaultdict
import re
from itertools import product

def solution(user_id, banned_id):
    d = defaultdict(list)
    banned_regexes = deque()
    for ban in banned_id:
        b = ban.replace('*', "[a-z0-9]")
        banned_regexes.append(re.compile(b))
    
    for user in user_id:
        for idx, banned_regex in enumerate(banned_regexes):
            if banned_regex.fullmatch(user):
                d[idx].append(user)
    cases = list(d.values())
    answers = deque()
    for case in product(*cases):
        s_case = set(case)
        if len(case) == len(s_case) and s_case not in answers:
            answers.append(s_case)
    return len(answers)
