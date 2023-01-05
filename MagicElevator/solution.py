def over_half(n, ans, storey):
    return ans + n, storey + n
    
def under_half(n, ans, storey):
    return ans + n, storey - n    

def solution(storey):
    idx = 0
    answer = 0
    while storey != 0:
        idx = storey % 10
        if idx == 0: 
            pass
        elif idx < 5:
            answer, storey = under_half(idx, answer, storey)
        elif idx == 5:
            if (storey // 10) % 10 >= 5:
                answer, storey = over_half(10 - idx, answer, storey)
            else:
                answer, storey = under_half(idx, answer, storey)
        else:
            answer, storey = over_half(10 - idx, answer, storey)
            
        if not storey == 0:
            storey = storey // 10
        
    return answer