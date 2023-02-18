from datetime import datetime
import re

def solution(m, musicinfos):
    
    musics = []
    for i in ["C", "D", "F", "G", "A"]:
        m = re.sub(f"{i}#", i.lower(), m)
        
    for music in musicinfos:
        music = music.split(",")
        start = datetime.strptime(music[0], "%H:%M")
        end = datetime.strptime(music[1], "%H:%M")
        diff = (end-start).seconds//60 + 1
        
        for i in ["C", "D", "F", "G", "A"]:
            music[3] = re.sub(f"{i}#", i.lower(), music[3])
            
        l = len(music[3])
        
        d, r = divmod(diff, l)
        melody = music[3]*d + music[3][:r]
        i = melody.find(m)
        
        if i != -1:
            musics.append((music[2], diff))
            
    if musics:
        musics.sort(key=lambda x: -x[1])
        return musics[0][0]
    else: 
        return "(None)"

