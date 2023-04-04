from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_d = defaultdict(int)
    play_d = defaultdict(list)
    
    for i in range(len(genres)):
        genre_d[genres[i]] += plays[i]
        if len(play_d[genres[i]]) == 2:
            if play_d[genres[i]][0][1] < plays[i]:
                play_d[genres[i]][0] = (i, plays[i])
                play_d[genres[i]].sort(key=lambda x: (x[1], -x[0])) 
        else:
            play_d[genres[i]].append((i, plays[i]))
            play_d[genres[i]].sort(key=lambda x: (x[1], -x[0]))
    top_genres = map(lambda x: x[0], sorted(list(genre_d.items()), key=lambda x: x[1], reverse=True))
    
    for genre in top_genres:
        for i in range(len(play_d[genre])-1, -1, -1):
            answer.append(play_d[genre][i][0])
    return answer
