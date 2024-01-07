import sys 
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check_dfs(n, graph, dx, dy, x, y, k):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[ny][nx] > k:
            graph[ny][nx] = 0
            check_dfs(n, graph, dx, dy, nx, ny, k)
        
def main():
    #이동 방향 -> 상, 하, 좌, 우
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]
    
    safe_area = []
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    #층의 범위
    max_value = max([max(row) for row in graph])
    
    #비가 안 내리는 경우 ~ 층의 높이까지 비가 내리는 경우
    for k in range(0, max_value):
        count = 0
        copy_graph = copy.deepcopy(graph)
        for j in range(n):
            for i in range(n):
                if copy_graph[j][i] > k:
                    check_dfs(n, copy_graph, dx, dy, i, j, k)
                    count += 1
        safe_area.append(count)
                
    print(max(safe_area))

if __name__ == "__main__" :
    main()