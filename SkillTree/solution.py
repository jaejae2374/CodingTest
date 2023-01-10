def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        skill_ = skill
        for t in tree:
            if t in skill_:
                if t == skill_[0]:
                    skill_ = skill_[1:]
                else:
                    break
        else:
            answer += 1    
    return answer
