import sys
from collections import deque
input = sys.stdin.readline

def maze(x, y):
  # 너비 우선 탐색
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1] 

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      # 벽이므로 진행 불가
      if graph[nx][ny] == 0:
        continue
      
      # 벽이 아니므로 이동
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[n - 1][m - 1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    print(maze(0, 0))
    
'''
문제: 미로 탐색
알고리즘: 그래프 이론, 그래프 탐색, 너비 우선 탐색
느낀점: 상하좌우 방향 지정하는 방법, 탐색 조건(주어진 그래프 범위 벗어나지 않기) 잘 기억하기
'''