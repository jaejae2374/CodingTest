def solution(n, arr1, arr2):
    answer = []
    new_arr1, new_arr2 = [], []
    for a1, a2 in zip(arr1, arr2):
        a1 = bin(a1)[2:]; a2 = bin(a2)[2:]
        new_arr1.append("{:0>{}}".format(a1, n))
        new_arr2.append("{:0>{}}".format(a2, n))
    for ar1, ar2 in zip(new_arr1, new_arr2):
        answer.append(''.join(map(lambda x: "#" if (int(x[0]) or int(x[1])) else " ", zip(ar1, ar2))))
    return answer
