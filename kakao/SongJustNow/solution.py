from datetime import datetime

def solution(m, musicinfos):
    musics = []
    for music in musicinfos:
        music = music.split(",")
        start = datetime.strptime(music[0], "%H:%M")
        end = datetime.strptime(music[1], "%H:%M")
        diff = (end-start).seconds//60
        l = len(music[3])
        
        d, r = divmod(diff, l)
        melody = music[3]*d + music[3][:r]
        i = melody.find(m)
        if i != -1:
            if melody[i+len(m)] != "#":
                musics.append((music[2], diff))
    if musics:
        musics.sort(key=lambda x: -x[1])
        return musics[0][0]
    else: 
        return "(None)"

