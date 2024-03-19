from collections import deque


def solution(maps):
    waysToGo = []

    n = len(maps)
    m = len(maps[0])

    # mlist = [0 for _ in range(m)]
    visited = [[0]*m for _ in range(n)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = 1

    while (queue):
        x, y, val = queue.popleft()

        if x == n - 1 and y == m - 1:
            waysToGo.append(val)
            continue

        if y - 1 >= 0 and maps[x][y - 1] == 1 and visited[x][y - 1] == 0:  # left
            queue.append((x, y - 1, val + 1))
            visited[x][y - 1] = 1
        if y + 1 <= m - 1 and maps[x][y + 1] == 1 and visited[x][y + 1] == 0:  # right
            queue.append((x, y + 1, val + 1))
            visited[x][y + 1] = 1
        if x - 1 >= 0 and maps[x - 1][y] == 1 and visited[x - 1][y] == 0:  # up
            queue.append((x - 1, y, val + 1))
            visited[x - 1][y] = 1
        if x + 1 <= n - 1 and maps[x + 1][y] == 1 and visited[x + 1][y] == 0:  # down
            queue.append((x + 1, y, val + 1))
            visited[x + 1][y] = 1

    print(waysToGo)
    if len(waysToGo) != 0:
        return min(waysToGo)
    else:
        return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))