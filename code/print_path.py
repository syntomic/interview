dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)] ## 顺时针
cant_pos = [(1, 0), (1, 1), (2, 2)]


def passable(N, M, cant_pos, pos):
    is_in_N = (0 <= pos[0] <= N)
    is_in_M = (0 <= pos[1] <= M)
    is_not_in_cant_pos = ( pos not in cant_pos) 

    return is_in_N and is_in_M and is_not_in_cant_pos

def print_path(N, M, cant_pos, start, end):
    if start == end:
        return [[start]]

    paths = []
    cant_pos.append(start)

    for i in range(4):
        nextp = start[0] + dirs[i][0], start[1] + dirs[i][1]
        if passable(N, M, cant_pos, nextp):
            _ = print_path(N, M, cant_pos.copy(), nextp, end)  ## 保持 cant_pos一致
            if _: ## [[path1], [path2]...]
                for i in range(len(_)):
                    paths.append([start] + _[i])

    return paths

print(print_path(3, 3, cant_pos, (0, 0), (3, 3)))
print(cant_pos) 