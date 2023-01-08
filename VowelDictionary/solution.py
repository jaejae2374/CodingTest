from itertools import *

def solution(word):
    dataset = ['A', 'E', 'I', 'O', 'U', '']

    dictionary = list(set(map(lambda x: ''.join(x), list(product(dataset, repeat=5)))))
    dictionary.sort()

    answer = dictionary.index(word)
    return answer
