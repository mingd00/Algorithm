import sys 
input = sys.stdin.readline
from collections import deque

def snake(x, y):
    time, total_time = 0, 0
    degree = 0
    q = deque()
    q.append((0, 0))

    for direction in directions:
        for _ in range(int(direction[0])-total_time):
            x = x + dx[degree]
            y = y + dy[degree]
            time += 1
            if 0 <= x < N and 0 <= y < N and visited[x][y] == 0:
                visited[x][y] = 1
                q.append((x, y))
                if [x+1, y+1] not in apples:
                    i, j = q.popleft()
                    visited[i][j] = 0
                else:
                    apples.remove([x+1, y+1])
            else:
                return time
        if direction[1] == 'D': # 오른쪽 회전
                degree = (degree + 1) % 4
        elif direction[1] == 'L': # 왼쪽 회전
                degree = (degree + 3) % 4
        total_time = time
        
    # 뱡향 변환 정보가 모두 끝나면 마지막 방향으로 계속 전진
    while True:
            x = x + dx[degree]
            y = y + dy[degree]
            time += 1
            if 0 <= x < N and 0 <= y < N and visited[x][y] == 0:
                visited[x][y] = 1
                q.append((x, y))
                if [x+1, y+1] not in apples:
                    i, j = q.popleft()
                    visited[i][j] = 0
                else:
                    apples.remove([x+1, y+1])
            else:
                return time

if __name__ == "__main__" : 
    N = int(input())
    K = int(input())
    apples = [list(map(int, input().split())) for _ in range(K)]
    L = int(input())
    directions = [list(input().split()) for _ in range(L)]
    
    # 동, 남, 서, 북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    
    print(snake(0, 0))