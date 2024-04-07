import sys 
input = sys.stdin.readline
from collections import deque

def bfs(i, j):
    change = []
    q = deque()
    q.append((i, j))
    change.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:   
                if L <= abs(village[x][y]-village[nx][ny]) <= R:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    change.append((nx, ny))
                    
    if len(change) > 1:
        avg = sum(village[a][b] for a, b in change) // len(change)
        for a, b in change:
            village[a][b] = avg  
        return 1
    else:
        return 0
                        
if __name__ == "__main__" : 
    N, L, R = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    result = 0
    
while True:
    count = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                count += bfs(i, j)
              
    if count > 0:
        result += 1
    else:
        print(result)     
        break
                    
        
                

    
    
    