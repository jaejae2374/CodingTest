#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    primes = [True]*(b+1)
    primes[0] = False; primes[1] = False
    for i in range(2, b+1):
        cnt = 2
        while i*cnt<=b:
            primes[i*cnt] = False
            cnt+=1
    for i in range(2, b):
        if i**2>b:
            break
        if primes[i]:
            if a<=i**2<=b:
                answer+=1
            if a<=i**3<=b:
                answer+=1
        
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
