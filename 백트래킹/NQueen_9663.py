import sys 
input = sys.stdin.readline

# 행 단위로 탐색
def dfs(row, N, v1, v2, v3):
    global answer
    
    if row == N:
        answer += 1
        return
    
    for col in range(N):
        if v1[col] == v2[row - col] == v3[row + col] == 0:
            v1[col] = v2[row - col] = v3[row + col] = 1
            dfs(row+1, N, v1, v2, v3)
            v1[col] = v2[row - col] = v3[row + col] = 0     

def main() :
    N = int(input())
    
    # 열 방문 체크
    v1 = [0] * N
    # 왼쪽 위 대각선 방문 체크
    v2 = [0] * (2*N)
    # 오른쪽 위 대각선 방문 체크
    v3 = [0] * (2*N)
    
    dfs(0, N, v1, v2, v3)

if __name__ == "__main__" :
    answer = 0
    main()
    print(answer)