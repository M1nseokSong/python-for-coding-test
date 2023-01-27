# bfs로 풀어야 겠다는 아이디어를 떠올리는 것이 중요한 것 같다. 

from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        nx, ny = queue.popleft()
        for _ in range(4):
            for_x, for_y = nx + dx[_], ny + dy[_]
            if (for_x <= -1) or (for_x >= n) or (for_y <= -1) or (for_y >= m):
                continue
            if miro[for_x][for_y] == 0:
                continue
            if miro[for_x][for_y] == 1:
                queue.append([for_x, for_y])
                miro[for_x][for_y] = miro[nx][ny] + 1
            if (nx + dx[_] == n-1) and (ny + dy[_] == m-1):
                break
    #print(miro)
    return miro[n-1][m-1]

print(bfs(0, 0))
