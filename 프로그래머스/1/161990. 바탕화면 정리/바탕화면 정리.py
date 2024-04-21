def solution(wallpaper):
    answer = []
    col = []
    row = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                col.append(i) # col 리스트에 샵들의 시작점들이 들어감
                row.append(j) # row 리스트에는 샵들의 끝점들이 들어감
    return [min(col), min(row), max(col)+1, max(row)+1]