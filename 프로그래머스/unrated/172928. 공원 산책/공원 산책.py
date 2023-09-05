def solution(park, routes):
# park 구성
# 출발 지점 : S
# 길 0, 장애물 1로 코딩
    map_array = []
    park_list = ["S", "O", "X"]
    for i in range(len(park)):
        park_i = park[i]
        len_i = len(park_i) #park[i] 원소의 길이
        i_list = []
        for j in range(len_i):
            if park_i[j] == "S":
                i_list.append("S")
                r, c = i, j # r,c : 출발지점 좌표(r,c)
            elif park_i[j] == "O":
                i_list.append(0)
            else:
                i_list.append(1)
        map_array.append(i_list)

    directions = ["N", "S", "W", "E"]
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]

    for k in routes:
        error = 0
        d = k[0] # 방향 : N S W E
        step = int(k[2]) # 걸음수

        if d in directions:
            idx = directions.index(d)
            next_row = r + d_row[idx]*step
            next_col = c + d_col[idx]*step

            if next_row < 0 or next_row > (len(map_array)-1):
                continue

            elif next_col < 0 or next_col > (len(map_array[1])-1):
                continue

            elif d_row[idx]*step != 0:
                for l in range(1, step+1):
                    next_row = r + d_row[idx]*l
                    if map_array[next_row][next_col] == 1:
                        error += 1

            elif d_col[idx]*step != 0:
                for l in range(1, step+1):
                    next_col = c + d_col[idx]*l
                    if map_array[next_row][next_col] == 1:
                        error += 1
            if error > 0:
                r,c = r,c
            elif error == 0:
                r = next_row
                c = next_col

    result = [r,c]
    return result