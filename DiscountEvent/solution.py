from collections import Counter

def solution(want, number, discount):
    want_dict = {}
    answer = 0
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    for i in range(len(discount)-len(want)+1):
        if i <= len(discount)-10:
            c = Counter(discount[i:i+10])
        else:
            c = Counter(discount[i:])
        
        for want_item in want_dict.keys():
            if want_item in c:
                if want_dict[want_item] > c[want_item]:
                    break
            else:
                break
        else:
            answer+=1
    
    return answer