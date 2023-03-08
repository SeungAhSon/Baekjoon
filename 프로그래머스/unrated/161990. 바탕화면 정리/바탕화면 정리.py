def solution(wallpaper):
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            for j in range(len(wallpaper[i])):
                if wallpaper[i][j]=="#":
                    x.append(i)
                    y.append(j)
    
    return [min(x), min(y), max(x)+1, max(y)+1]