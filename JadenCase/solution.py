def solution(s):
    sentences = s.split(' ')
    new_sentences = []
    for sen in sentences:
        new_sentences.append(sen.capitalize())
    answer = ' '.join(new_sentences)
    return answer
