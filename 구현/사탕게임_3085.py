import sys
input = sys.stdin.readline
from collections import Counter

# 연속 행 또는 열의 최대 길이 반환 
def check_cnt(n, target_list):
    global max_cnt
    
    for i in range(n):
        # 가로 방향 카운트
        cnt = 1
        for j in range(n-1):
            if target_list[i][j] == target_list[i][j+1]:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt
            
        # 세로 방향 카운트
        cnt = 1
        for j in range(n-1):
            if target_list[j][i] == target_list[j+1][i]:
                cnt += 1
            else:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt

# 모든 부분을 한번씩 교체
def change(n, board):
    # 가로 교체
    for i in range(n):
        for j in range(n-1):
            if board[i][j] != board[j+1][i]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                check_cnt(n, board)
                board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
    # 세로 교체
    for i in range(n):
        for j in range(n-1):
            if board[j][i] != board[j+1][i]:
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                check_cnt(n, board)
                board[j+1][i], board[j][i] = board[j][i], board[j+1][i]
            
if __name__ == "__main__":
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    max_cnt = 0
    
    change(n, board)
    print(max_cnt)
    
            