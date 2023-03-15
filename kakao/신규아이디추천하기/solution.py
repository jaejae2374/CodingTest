import re

def solution(new_id):
    correct_id = re.compile("[^a-z]|.|[0-9]|-|_")
    
    # 1
    new_id = new_id.lower()
    # 2
    id_ = re.sub("[^a-z.0-9-_]", "", new_id)
    # 3
    id_ = re.sub("[.]+", ".", id_)
    # 4
    if id_ and id_[0] == ".":
        id_ = id_[1:]
    if id_ and id_[-1] == ".":
        id_ = id_[:-1]
    # 5
    if not id_:
        id_ = "a"
    # 6
    if len(id_) >= 16:
        id_ = id_[:15]
    if id_ and id_[-1] == ".":
        id_ = id_[:-1]
    # 7
    if len(id_) <= 2:
        while len(id_) < 3:
            id_ += id_[-1]
    return id_
