import sys 
from collections import deque
input = sys.stdin.readline

#입력 -> 현재 아기 상어의 위치, 출력 -> 후보 리스트      
def bfs(n, graph, a, b):
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0]*n for _ in range(n)]
    vlist = []
    que = deque((a, b))
    
    visited[a][b] = 1
    
    while que:
        x, y = que.popleft()  
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            #아기 상어보다 작은 물고기 -> 잡아 먹음
            if graph[x][y] > graph[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                #시간, 위치
                vlist.append((visited[nx][ny] - 1, nx, ny))
            #아기 상어와 크기가 같은 물고기 or 물고기가 없을 때 -> 그냥 지나감
            elif graph[x][y] == graph[nx][ny] or graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))
                
    return sorted(vlist, key = lambda x: (x[0], x[1], x[2]))
            
         
def main() :
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    pos = []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                pos.append(i)
                pos.append(j)
    
    count = 0     

    i, j = pos
    size = [2, 0]
    
    while True:
        graph[i][j] = size[0]
        vlist = deque(bfs(i, j))
        
        if not vlist:
            break
        
        step, xx, yy = vlist.popleft()
        count += step
        size[1] += 1
        
        if size[0] == size[1]:
            size[0] += 1
            size[1] = 0
            
        graph[i][j] = 0
        i, j = xx, yy
    
    print(count)

if __name__ == "__main__" : 
    main()
    
import sys
from collections import deque

input = sys.stdin.readline


def bfs(r,c,shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    tmp = []
    while q:
        cur_r,cur_c = q.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0<= nr < n and 0<= nc < n and visited[nr][nc] == 0:
                if ocean[nr][nc] <= shark_size:
                    q.append((nr,nc))
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[cur_r][cur_c] + 1
                    
                    if ocean[nr][nc] < shark_size and ocean[nr][nc] != 0:
                        tmp.append((nr,nc,distance[nr][nc]))

    return sorted(tmp,key=lambda x: (-x[2],-x[0],-x[1]))

if __name__ == '__main__':
    n = int(input())
    ocean = [list(map(int,input().split())) for i in range(n)]
    dr = [0,0,1,-1] # 0 우 1 왼 2 하 3 상
    dc = [1,-1,0,0]
    exp = 0
    size = 2
    answer = 0
    for i in range(n):
        for j in range(n):
            if ocean[i][j] == 9:
                r, c = i, j

    while 1:
        shark = bfs(r,c,size)

        if len(shark) == 0:
            break
        
        nr,nc,dist =shark.pop()
        answer += dist
        ocean[r][c],ocean[nr][nc] = 0,0
        r,c = nr,nc
        exp += 1
        if exp == size:
            size += 1
            exp = 0
    print(answer)