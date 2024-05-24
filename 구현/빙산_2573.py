import sys
input = sys.stdin.readline
from collections import deque
    
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    sea_list = []
    
    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if not iceberg[nx][ny]:
                    sea += 1
                elif iceberg[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny)) 
                    visited[nx][ny] = 1
        if sea > 0:
            sea_list.append((x, y, sea)) 
    # 빙산 녹이기
    for x, y, sea in sea_list:
        iceberg[x][y] = max(0, iceberg[x][y]-sea)
            
    return 1  

if __name__ == "__main__":
    N, M = map(int, input().split())
    iceberg = [list(map(int, input().split())) for _ in range(N)]
    
    ice_loc = []
    for i in range(N):
        for j in range(M):
            if iceberg[i][j]:
                ice_loc.append((i, j))
    year = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while ice_loc:
        visited = [[0]*M for _ in range(N)]
        del_list = []
        count = 0
        for i, j in ice_loc:
            if iceberg[i][j] and not visited[i][j]:
                count += bfs(i, j)
            # 탐색 후 다 녹은 빙산 체크
            if iceberg[i][j] == 0:
                del_list.append((i, j))
        if count > 1:
            print(year)
            break
        
        # 녹은 빙산 ice_loc에서 제거
        ice_loc = sorted(list(set(ice_loc)-set(del_list)))
        year += 1
    
    if count < 2:
        print(0)
