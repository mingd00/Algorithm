import sys
from collections import deque

input = sys.stdin.readline

#현재 아기 상어의 위치 input, 먹을 수 있는 물고기들의 리스트 return
def bfs(r,c,shark_size):
    visited = [[0] * n for _ in range(n)]
    que = deque()
    que.append((r,c))
    tmp = []
    
    while que:
        cur_r, cur_c = que.popleft()
        
        #상하좌우 탐색
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0:
                #물고기가 상어보다 작거나 같을 때
                if ocean[nr][nc] <= shark_size:
                    que.append((nr,nc))
                    #거리 업데이트
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    
                    #물고기가 상어보다 작을 때
                    if ocean[nr][nc] < shark_size and ocean[nr][nc] != 0:
                        #거리, 좌표 append
                        tmp.append((visited[nr][nc], nr, nc))

    #오름차순 정렬(거리 -> y좌표 -> x좌표 순으로 오름차순 정렬)
    return sorted(tmp, key = lambda x: (x[0],x[1],x[2]), reverse=True)

if __name__ == '__main__':
    n = int(input())
    ocean = [list(map(int, input().split())) for _ in range(n)]
    
    #상하좌우
    dr = [0,0,1,-1] 
    dc = [1,-1,0,0]
    
    exp = 0
    shark_size = 2
    time = 0
    
    for i in range(n):
        for j in range(n):
            if ocean[i][j] == 9:
                r, c = i, j

    while True:
        #먹을 수 있는 물고기들의 리스트(거리, x좌표, y좌표)
        shark = bfs(r, c, shark_size)

        #더 이상 먹을 물고기가 없는 경우
        if len(shark) == 0:
            break
        
        #물고기를 먹는데 걸린 시간, 현재 위치 업데이트 
        dist, nr, nc = shark.pop()
        time += dist
        ocean[r][c], ocean[nr][nc] = 0,0
        r, c = nr, nc
        
        #먹은 물고기 수가 상어의 크기와 같다면 상어의 크기 += 1
        exp += 1
        if exp == shark_size:
            shark_size += 1
            exp = 0
            
    print(time)