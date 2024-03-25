import sys 
input = sys.stdin.readline

def dfs(x, y, depth, val):
    global answer
    if depth == 4:
        answer = max(answer, val)
    elif (val + max_val*(4-depth)) <= answer:
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                # T자 도형 탐색 -> depth=2일 때 커서를 고정
                if depth == 2:
                    dfs(x, y, depth+1, val+graph[nx][ny])
                dfs(nx, ny, depth+1, val+graph[nx][ny])
                visited[nx][ny] = 0
    
if __name__ == "__main__" : 
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    # 가지치기 -> 4번을 다 확인하지 않아도 되는 경우 연산 횟수 감소
    max_val = max(map(max, graph))
    answer = -1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(n):
        for j in range(m):
            visited[i][j] = 1
            dfs(i, j, 1, graph[i][j])
            visited[i][j] = 0
            
    print(answer)