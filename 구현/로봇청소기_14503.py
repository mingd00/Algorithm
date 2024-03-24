import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y, depth):
    global answer, d
    # 모든 방향을 다 탐색 했다면
    if depth == 4:
        # 후진
        nx = x + dx[(d-2) % 4]
        ny = y + dy[(d-2) % 4]
        if room[nx][ny] == 2:
            dfs(nx, ny, 0)
        else:
            print(answer)
            exit(0)
    
    nx = x + dx[(d-1) % 4]
    ny = y + dy[(d-1) % 4]
    
    if room[nx][ny] == 0:
        room[nx][ny] = 2
        answer += 1
        # 반시계 방향으로 방향 전환
        d = (d-1) % 4  
        dfs(nx, ny, 0)
    elif room[nx][ny] == 1 or room[nx][ny] == 2:
        d = (d-1) % 4
        dfs(x, y, depth+1)

if __name__ == "__main__" : 
    n, m = map(int, input().split())
    i, j, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 로봇 청소기가 있는 칸은 항상 빈 칸
    answer = 1
    room[i][j] = 2
    
    dfs(i, j, 0)
    