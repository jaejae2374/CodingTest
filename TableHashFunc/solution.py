def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    
    idx = row_begin
    answer = 0
    
    for tup in data[row_begin-1:row_end]:
        answer = answer ^ sum(map(lambda x: x%idx, tup))
        idx+=1
    return answer