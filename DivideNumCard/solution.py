import math

def get_gcd(arr):
    g = arr[0]
    for i in range(len(arr)):
        g = math.gcd(g, arr[i])
    return g

def check_cd(n, arr):
    if {0} & set(map(lambda x: x%n, arr)):
        return False
    return True
    
def solution(arrayA, arrayB):
    first = [arrayA, arrayB]
    second = [arrayB, arrayA]
    answer = 0
    
    for i in range(2):
        gcd = get_gcd(first[i])
        if gcd and check_cd(gcd, second[i]):
            answer = max(answer, gcd)
    return answer
