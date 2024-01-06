import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

def check_dfs(graph, w, h, dx, dy, x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        #범위 체크
        if nx >= 0 and ny >= 0 and nx < w and ny < h and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            check_dfs(graph, w, h, dx, dy, nx, ny)
            
            
def check_bfs(graph, w, h, dx, dy, x, y):
    que = deque()
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
    
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 체크
            if nx >= 0 and ny >= 0 and nx < w and ny < h and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                que.append((nx, ny))
            
    return 

def main():
    #탐색 방향 지정 -> 상, 하, 좌, 우, 대각선
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        count = 0

        graph = [list(map(int, input().split())) for _ in range(h)]    
        
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    check_dfs(graph, w, h, dx, dy, j, i)
                    count += 1
        print(count)    

if __name__ == "__main__" :
    main()