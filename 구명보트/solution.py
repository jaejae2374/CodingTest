from collections import deque

def solution(people, limit):
    people.sort()
    deq = deque(people)
    answer = 0
    while deq:
        kg = deq.pop()
        answer += 1
        idx = 0
        for person in deq:
            if person + kg <= limit:
                kg += person
                idx += 1
            else:
                break
        for i in range(idx): deq.popleft()
    return answer
