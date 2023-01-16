def check(arr, row, col):
    dirs = [1, -1]
    for d in dirs:
        if 0 <= row+d < 5:
            if arr[row+d][col] == 'P':
                return False
            elif arr[row+d][col] == 'O':
                if 0<= row+(2*d) < 5:
                    if arr[row+(2*d)][col] == 'P':
                        return False
                for d2 in dirs:
                    if 0 <= col+d2 < 5:
                        if arr[row+d][col+d2] == 'P':
                            return False
        if 0 <= col+d < 5:
            if arr[row][col+d] == 'P':
                return False
            elif arr[row][col+d] == 'O':
                if 0<= col+(2*d) < 5:
                    if arr[row][col+(2*d)] == 'P':
                        return False
                for d2 in dirs:
                    if 0 <= row+d2 < 5:
                        if arr[row+d2][col+d] == 'P':
                            return False
    return True
    
def solution(places):
    answer = []
    for place in places:
        isSuccess = True
        for row in range(0, len(place)):
            if "P" in place[row]:
                for col in range(0, len(place[0])):
                    if place[row][col] == 'P':
                        isSuccess = check(place, row, col)
                        if not isSuccess:
                            answer.append(0)
                            break
                if not isSuccess:
                    break
        else:
            answer.append(1)
        
    return answer
