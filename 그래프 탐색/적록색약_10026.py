import sys
input = sys.stdin.readline
import copy
from collections import deque

def check_bfs(n, graph, dx, dy, x, y, start):
    que = deque()
    que.append((x, y))
    
    # 시작 정점은 방문한 것으로 가정
    graph[y][x] = '0'
    
    while que:
        a, b = que.popleft()    
          
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[ny][nx] == start:
                graph[ny][nx] = '0'
                que.append((nx, ny))   


def main():
    count = 0
    color_blindness_count = 0
    
    # 상, 하, 좌, 우
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    
    # 적록색약 리스트 새로 생성('R', 'G' -> 'C')
    color_blindness_graph = [['0']*n for _ in range(n)]
    # 그냥 copy를 하면 원래 graph 값이 바뀜
    # color_blindness_graph = copy.deepcopy(graph)

    for j in range(n):
        for i in range(n):
            if graph[j][i] == 'R' or graph[j][i] == 'G':
                color_blindness_graph[j][i] = 'C'
            else:
                color_blindness_graph[j][i] = 'B'
    
    # 적록색약X BFS
    for j in range(n):
        for i in range(n):   
            if graph[j][i] != '0':   
                check_bfs(n, graph, dx, dy, i, j, graph[j][i])
                count += 1
    
    # 적록색약O BFS            
    for j in range(n):
        for i in range(n):   
            if color_blindness_graph[j][i] != '0':   
                check_bfs(n, color_blindness_graph, dx, dy, i, j, color_blindness_graph[j][i])
                color_blindness_count += 1       
    
    print(count, color_blindness_count)
    
  
if __name__ == "__main__":
    main()