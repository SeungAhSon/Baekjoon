def time_to_sec(time_str:str)->int:
    minutes, sec = map(int, time_str.split(":"))
    return minutes*60+sec
    
def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    for com in commands:
        if op_start<=pos and pos<=op_end: pos = op_end
        if com=="prev":
            pos-=10
            if pos<0: pos = 0
        else:
            pos+=10
            if pos>video_len: pos = video_len
    if op_start<=pos and pos<=op_end: pos = op_end
    minute = pos // 60
    sec = pos % 60
    return f"{minute:02}:{sec:02}"