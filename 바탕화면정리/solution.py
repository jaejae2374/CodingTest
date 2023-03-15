def solution(wallpaper):
    rows = []; cols = []
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == "#":
                rows.append(row)
                cols.append(col)
    return [min(rows), min(cols), max(rows)+1, max(cols)+1]
