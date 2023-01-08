def solution(elements):
    elements_ = elements + elements
    results = []
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            results.append(sum(elements_[j:j+i]))
    answer = len(set(results))
    return answer