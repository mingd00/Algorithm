import sys 
input = sys.stdin.readline
from collections import deque

def dice(i, j):
    dice_num = [0 for _ in range(7)]
    col = deque([2, 1, 5, 6])
    row = deque([4, 1, 3])
    q = deque()
    q.append((i, j))
    for o in orders:
        x, y = q.popleft()
        nx = x + dx[o-1]
        ny = y + dy[o-1]
        if 0 <= nx < N and 0 <= ny < M:
            q.append((nx, ny))
            if o == 1:
                t = row.popleft()
                row.append(t)
                col[1] = row[1]
         
                t = row[2]
                row[2] = col[3]
                col[3] = t  
                
            elif o == 2:
                t = row.pop()
                row.appendleft(t)
                col[1] = row[1]
                
                t = row[0]
                row[0] = col[3]
                col[3] = t        
                        
            elif o == 3:
                t = col.pop()
                col.appendleft(t)
                row[1] = col[1]
                
            elif o == 4:
                t = col.popleft()
                col.append(t)
                row[1] = col[1]
            
            if board[nx][ny] > 0:
                dice_num[col[1]] = board[nx][ny]
                board[nx][ny] = 0
            else:
                board[nx][ny] = dice_num[col[1]]
                
            print(dice_num[col[3]])
        else:
            q.append((x, y))

if __name__ == "__main__" : 
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))
    
    # 동, 서, 북, 남
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    dice(x, y)
    