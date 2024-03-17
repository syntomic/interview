# 迷宫 用二维数组来表示，0表示可以走，1表示障碍。可以上下左右四个方向移动

# 0,0,0,0,0
# 0,1,0,1,0
# 0,1,1,0,0
# 0,1,1,0,1
# 0,0,0,0,0

# 起点0,0 -> 终点4,4

# 求最短路径长度，并打印出路径
from collections import deque

def solution():
    """generate by chatgpt"""
    maze = [[0,0,0,0,0],
            [0,1,0,1,0],
            [0,1,1,0,0],
            [0,1,1,0,1],
            [0,0,0,0,0]]

    start = (0, 0)
    end = (4, 4)

    queue = deque([start])
    visited = set([start])

    predecessor = {start: None}
    while queue:
        current = queue.popleft()
        if current == end:
            break

        x, y = current
        for dx, dy in [(0, 1), (0,-1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if 0<= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0 and (next_x, next_y) not in visited:
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                predecessor[(next_x, next_y)] = current

    if end not in predecessor:
        print("无法到达终点")
    else:
        path = []
        current = end
        while current:
            path.append(current)
            current = predecessor[current]

    path.reverse()
    print("最短路径长度为:", len(path)-1)
    print("最短路径为:", path)

if __name__ == "__main__":
    solution()