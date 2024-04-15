import sys 
input = sys.stdin.readline
from collections import deque

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0
    
    while q:
        # depth로 체크해야 하기 때문에 큐에 들어있는 값만큼 탐색하고 count+=1
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10:
                print(-1)
                return 
            if board[rx][ry] == 'O':
                print(count)
                return
            
            for i in range(4):
                # 빨간 구슬 탐색
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    
                    if board[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    elif board[nrx][nry] == 'O':
                        break
                # 파란 구슬 탐색
                nbx, nby = bx, by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    
                    if board[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    elif board[nbx][nby] == 'O':
                        break
                # 파란 구슬이 구멍에 들어가면 안됨 -> 넘기기
                if board[nbx][nby] == 'O':
                    continue
                
                # 파란 구슬과 빨간 구슬이 같이 있을 때
                if nrx == nbx and nry == nby:
                    # 좌표 차이가 큰 쪽이 나중에 출발 -> 이전 좌표로 돌려주기
                    if abs(nrx-rx)+abs(nry-ry) > abs(nbx-bx)+abs(nby-by):
                        nrx -= dx[i]
                        nry -= dy[i]     
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                # 방문하지 않았다면 큐, 방문 리스트에 추가        
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1                        
    print(-1)            

if __name__ == "__main__" : 
    N, M = map(int, input().split())
    board = [input().rstrip() for _ in range(N)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    
    bfs(rx, ry, bx, by)