def solution(cards1, cards2, goal):
    
    while goal:
        c1 = cards1[0] if cards1 else None
        c2 = cards2[0] if cards2 else None
        next_word = goal.pop(0)
        if c1 == next_word:
            cards1.pop(0)
        elif c2 == next_word:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
