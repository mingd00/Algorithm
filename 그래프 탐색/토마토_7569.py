import sys
input = sys.stdin.readline
from collections import deque

def tomato_bfs(row, col, height, graph, dh, dx, dy):
    que = deque()
    for k in range(height):
        for i in range(col):
            for j in range(row):
                if graph[k][i][j] == 1:
                    que.append((j,i,k))
               
    while que:
        x, y, h = que.popleft()
        
        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and ny >= 0 and nh >= 0 and nx < row and ny < col and nh < height and graph[nh][ny][nx] == 0:
                graph[nh][ny][nx] = graph[h][y][x] + 1
                que.append((nx, ny, nh))
                
    return graph


def main():
    row, col, height = map(int, input().split())
    graph = [[list(map(int, input().split())) for _ in range(col)] for _ in range(height)]
    
    #뱡향 지정 -> 앞, 뒤, 상, 하, 좌, 우
    dh = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    
    new_graph = tomato_bfs(row, col, height, graph, dh, dx, dy)
    
    if any(any(0 in element for element in row) for row in new_graph):
        print(-1)
    else:
        result = max(max(max(element) for element in row) for row in new_graph)
        print(result-1)

if __name__ == "__main__":
    main()