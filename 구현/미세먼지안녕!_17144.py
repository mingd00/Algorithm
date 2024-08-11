import sys
input = sys.stdin.readline

def dust_diffusion():
    # 미세먼지 확산
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_board = [[0] * C for _ in range(R)]
    new_board[a1][0] = -1
    new_board[a2][0] = -1
    
    for x in range(R):
        for y in range(C):
            if board[x][y] > 0:
                new_board[x][y] += board[x][y]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        new_board[nx][ny] += board[x][y] // 5
                        new_board[x][y] -= board[x][y] // 5
    return new_board

def air_purifier():
    # 위쪽 순환-> 반시계 방향
    # 위에 값 가져오기(청정기 윗 부분 만큼)
    for x in range(a1-1, 0, -1):
        board[x][0] = board[x-1][0]
    # 오른쪽 값 가져오기(가로 길이만큼)
    for y in range(C-1):
        board[0][y] = board[0][y+1]
    # 아래 값 가져오기(청정기와 높이가 같아질 때까지)
    for x in range(a1):
        board[x][-1] = board[x+1][-1]
    # 왼쪽 값 가져오기(가로 길이만큼)
    for y in range(C-1, 0, -1):
        board[a1][y] = board[a1][y-1]

    # 아래쪽 순환-> 시계 방향, 아래->오른쪽->위->왼쪽 순으로 값 가져오기
    for x in range(a2+1, R-1):
        board[x][0] = board[x+1][0]
    for y in range(C-1):
        board[-1][y] = board[-1][y+1]
    for x in range(R-1, a2, -1):
        board[x][-1] = board[x-1][-1]
    for y in range(C-1, 0, -1):
        board[a2][y] = board[a2][y-1]

    # 공기청정기에서 나온 바람은 미세 먼지가 없는 바람이므로 0으로 초기화
    board[a1][1] = 0
    board[a2][1] = 0

if __name__ == "__main__":
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    
    for i in range(R):
        if board[i][0] == -1:
            # 반시계, 시계
            a1, a2 = i, i+1 
            break
    
    for _ in range(T):
        board = dust_diffusion()
        air_purifier()

    # 결과 출력
    ans = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                ans += board[i][j]
    print(ans)