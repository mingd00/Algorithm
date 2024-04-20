import sys 
input = sys.stdin.readline

# 낚시왕 이동
def catch(y, board):
    answer = 0
    for i in range(R):
        # 땅과 제일 가까운 상어
        if board[i][y]:
            answer = board[i][y][0][2]
            board[i][y] = []
            break
    return answer, board 

# 상어 이동
def move(board):
    # 상어 이동 임시배열
    tmp = [[[]for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                x, y, = i, j
                s, d, z = board[i][j][0]
                dis = s
                # 속력만큼 이동
                while dis:
                    x, y = x + dx[d], y + dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        dis -= 1
                    # 범위를 벗어났을 떄
                    else:
                        x, y = x - dx[d], y - dy[d]
                        # 방향전환
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                tmp[x][y].append([s, d, z])
                    
    for i in range(R):
        for j in range(C):
            # 2개 이상의 상어가 한 칸에 있을 때
            if len(tmp[i][j]) >= 2:
                tmp[i][j].sort(key=lambda x: x[2], reverse=True)
                s, d, z = tmp[i][j][0]
                tmp[i][j] = [[s, d, z]]
                
    return tmp           
        
if __name__ == "__main__" : 
    R, C, M = map(int, input().split())
    board = [[[]for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        x, y, s, d, z = map(int, input().split())
        # 상어가 2마리 이상 한 칸에 존재하는 경우도 있으므로 append 해줘야 함
        board[x-1][y-1].append([s, d-1, z]) # 속력, 이동방향, 크기
        
    # 상하우좌
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    shark = 0
    for i in range(C):
        eat, board = catch(i, board)
        shark += eat
        board = move(board)
        
    print(shark)