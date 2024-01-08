import sys
input = sys.stdin.readline
from collections import deque

def tomato_bfs(row, col, h, graph, dx, dy):
    que = deque()
    for i in range(col * h):
        for j in range(row):
           if graph[i][j] == 1:
               que.append((j,i))
               
    while que:
        x, y = que.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = x + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < row and ny < col * h and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                que.append((nx, ny))
                
    return graph


def main():
    row, col, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(col * h)] 
    
    #뱡향 지정 -> 상, 하, 좌, 우, 앞, 뒤
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, col, -col]
    
    new_graph = tomato_bfs(row, col, h, graph, dx, dy)
    print(new_graph)
    
    if any((0 in row) for row in new_graph):
        print(-1)
    else:
        result = max([max(row) for row in new_graph])
        print(result - 1)

if __name__ == "__main__":
    main()