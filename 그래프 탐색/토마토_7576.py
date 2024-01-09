import sys 
input = sys.stdin.readline
from collections import deque

def tomato_bfs(w, h, graph, dx, dy):
    que = deque()
    #익은 토마토 위치 체크
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                que.append((j,i))
    
    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < w and ny < h and graph[ny][nx] == 0:
                graph[ny][nx] = graph[b][a] + 1
                que.append((nx, ny))
                
    return graph
                

def main():
    #방향 정의 -> 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]

    new_graph = tomato_bfs(w, h, graph, dx, dy)
    
    #탐색 그래프에 0이 존재한다면
    if any((0 in row) for row in new_graph):
        print(-1)
    else:
        result = max([max(row) for row in new_graph])
        print(result-1)

if __name__ == "__main__":
    main()