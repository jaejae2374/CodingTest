from datetime import datetime, timedelta

def solution(book_time):
    timeline = [0]*1440
    for book in book_time:
        start, end = book
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        if end_time.hour == 23 and end_time.minute >= 50:
            end_time = datetime.strptime("23:59", "%H:%M")
        else:
            end_time = end_time + timedelta(minutes=10)
        m = int((end_time - start_time).seconds / 60)
        s = start_time.hour*60 + start_time.minute
        for i in range(s, s+m):
            timeline[i] += 1
        
    return max(timeline)
