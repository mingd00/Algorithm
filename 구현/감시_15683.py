import sys 
input = sys.stdin.readline
from collections import deque

# 범위 체크
def check(row, col):
    return row < 0 or row >= N or col < 0 or col >= M

def init():
    q = deque()
    ans = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and graph[i][j] != 6:
                q.append((graph[i][j], i, j))
            # cctv가 아예 없는 경우 고려
            if graph[i][j] == 0: ans += 1
    return q, ans
    
def move(y, x, direc, graph_copy):
    # 각각 방향에 대해 전부 이동
    for d in direc:
        nx, ny = x, y
        
        while True:
            nx += dx[d]
            ny += dy[d]
            # 범위를 벗어났거나 벽을 만나면
            if check(ny, nx) or graph_copy[ny][nx] == 6:
                break
            # 빈 칸이 아니면
            if graph_copy[ny][nx] != 0:
                continue
            graph_copy[ny][nx] = '#'
            
# 사각지대 구하기 -> 여러 개의 답 중 가장 최솟값으로 업데이트
def zero_cnt(graph_copy):
    global ans
    cnt = 0
    for i in graph_copy:
        cnt += i.count(0)
    ans = min(ans, cnt)
    
def dfs(level, graph):
    graph_copy = [[j for j in graph[i]] for i in range(N)]
    
    if level == len(cctv):
        zero_cnt(graph_copy)
        # 전 상태로 돌아감
        return
    
    number, y, x = cctv[level]
    # number 번째 cctv에 대해 가능한 모든 방향을 순차적으로 고려
    for d in direction[number]:
        move(y, x, d, graph_copy)
        dfs(level+1, graph_copy)
        graph_copy = [[j for j in graph[i]] for i in range(N)]

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    # 남동북서 -> 남쪽을 시작으로 반시계 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 감시해야하는 모든 방향
    direction = {
        1: [[0], [1], [2], [3]],
        2: [[0, 2], [1, 3]],
        3: [[0, 1], [1, 2], [2, 3], [3, 0]],
        4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        5: [[0, 1, 2, 3]]
    }
    
    # cctv 좌표와 빈 칸 초기화
    cctv, ans = init()
    
    dfs(0, graph)
    print(ans)
    
                 

    
    
    