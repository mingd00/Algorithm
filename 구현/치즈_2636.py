import sys 
input = sys.stdin.readline
from collections import deque

def bfs(graph, i, j):
    global count, rlist
    count = 0
    rlist = []
    q = deque()
    q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    rlist.append((nx, ny))
                    count += 1
                
if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [[0]*M for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time, count = 0, 0
    rlist = []
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(graph, i, j)
                time += 1
                for r in rlist:
                    graph[r[0]][r[1]] = 0
                    visited = [[0]*M for _ in range(N)]
            
            for g in graph:
                if 1 not in g:
                    continue
                else:
                    break
            else:
                print(time)
                print(count)
                exit()
                



    