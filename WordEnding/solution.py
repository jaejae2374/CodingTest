def solution(n, words):
    db = set()
    turn = 1
    player = 0
    before_word = words[0][0]
    for word in words:
        player += 1
        if player == n+1:
            player = 1
            turn += 1
        before = len(db)
        db.add(word)
        if len(db) == before:
            return [player, turn]
        else:
            if before_word[-1] != word[0]:
                return [player, turn]
        before_word = word
    else:
        return [0, 0]
